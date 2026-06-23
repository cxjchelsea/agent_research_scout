#!/usr/bin/env python3
"""Compute CR, RG, WSD and Go/No-Go recommendation from pilot run_log.jsonl."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path

import yaml

from trajectory_schema import load_jsonl

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[1]


@dataclass
class ConditionMetrics:
    condition: str
    n_instances: int
    resolve_at_k_rate: float
    resolve_at_k_count: int
    mean_first_step_error_attempt1: float | None
    mean_first_step_error_retry: float | None
    contamination_rate: float | None
    mean_workspace_drift: float | None


@dataclass
class PilotMetrics:
    n_instances: int
    recovery_gap_pp: float
    world_reset_wins: int
    world_reset_win_rate: float
    recommendation: str
    thresholds: dict
    by_condition: dict[str, ConditionMetrics]
    per_instance: list[dict]
    warnings: list[str]


def validate_rows(rows: list[dict], cfg: dict, *, allow_mock: bool, allow_unvalidated: bool) -> list[str]:
    errors: list[str] = []
    warnings: list[str] = []
    modes = {row.get("run_mode", "unknown") for row in rows}

    if "mock" in modes and not allow_mock:
        errors.append("run_log contains mock rows; rerun with --allow-mock only for pipeline tests")

    has_real_rows = bool(modes - {"mock"})
    hook_validated = bool((cfg.get("state_control") or {}).get("hook_validated"))
    if has_real_rows and not hook_validated and not allow_unvalidated:
        errors.append("state_control.hook_validated=false; run validate_pilot_setup.py before real analysis")

    unresolved = [row for row in rows if row.get("resolved") is None]
    if unresolved:
        errors.append(f"{len(unresolved)} rows have resolved=null; parse SWE-bench evaluation before analysis")

    if any(row.get("first_step_error") is None for row in rows):
        warnings.append("some rows lack first_step_error; CR may be null or incomplete")
    if any(not row.get("workspace_hash") or not row.get("initial_workspace_hash") for row in rows):
        warnings.append("some rows lack workspace hashes; WSD may be null or incomplete")

    if errors:
        detail = "\n".join(f"- {error}" for error in errors)
        raise ValueError(f"Pilot log is not analysis-ready:\n{detail}")
    return warnings


def resolve_at_k(attempts: list[dict]) -> bool:
    return any(a.get("resolved") for a in attempts)


def compute_workspace_drift(attempts: list[dict]) -> float | None:
    drifts: list[float] = []
    for a in attempts:
        initial = a.get("initial_workspace_hash")
        current = a.get("workspace_hash")
        if initial and current and initial != current:
            drifts.append(1.0)
        elif initial and current:
            drifts.append(0.0)
    return sum(drifts) / len(drifts) if drifts else None


def first_step_error_rate(attempts: list[dict], attempt_nums: set[int]) -> float | None:
    subset = [a for a in attempts if a.get("attempt") in attempt_nums and a.get("first_step_error") is not None]
    if not subset:
        return None
    return sum(1 for a in subset if a["first_step_error"]) / len(subset)


def analyze_rows(rows: list[dict], thresholds: dict, warnings: list[str] | None = None) -> PilotMetrics:
    by_inst_cond: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for row in rows:
        by_inst_cond[(row["instance_id"], row["condition"])].append(row)

    instance_ids = sorted({r["instance_id"] for r in rows})
    conditions = ["dirty-retry", "clean-restart", "full-reset"]

    by_condition: dict[str, ConditionMetrics] = {}
    per_instance: list[dict] = []

    for cond in conditions:
        resolve_count = 0
        all_attempts: list[dict] = []
        for iid in instance_ids:
            attempts = sorted(by_inst_cond.get((iid, cond), []), key=lambda x: x.get("attempt", 0))
            if attempts:
                all_attempts.extend(attempts)
                if resolve_at_k(attempts):
                    resolve_count += 1

        n = len(instance_ids)
        rate = resolve_count / n if n else 0.0
        err1 = first_step_error_rate(all_attempts, {1})
        err_retry = first_step_error_rate(all_attempts, {2, 3})
        cr = (err_retry - err1) if (err1 is not None and err_retry is not None) else None

        drifts = []
        for iid in instance_ids:
            attempts = by_inst_cond.get((iid, cond), [])
            d = compute_workspace_drift(attempts)
            if d is not None:
                drifts.append(d)

        by_condition[cond] = ConditionMetrics(
            condition=cond,
            n_instances=n,
            resolve_at_k_rate=rate,
            resolve_at_k_count=resolve_count,
            mean_first_step_error_attempt1=err1,
            mean_first_step_error_retry=err_retry,
            contamination_rate=cr,
            mean_workspace_drift=sum(drifts) / len(drifts) if drifts else None,
        )

    dirty = by_condition["dirty-retry"].resolve_at_k_rate
    clean = by_condition["clean-restart"].resolve_at_k_rate
    full = by_condition["full-reset"].resolve_at_k_rate
    rg_pp = (clean - dirty) * 100

    world_reset_wins = 0
    for iid in instance_ids:
        b_attempts = by_inst_cond.get((iid, "clean-restart"), [])
        c_attempts = by_inst_cond.get((iid, "full-reset"), [])
        b_res = resolve_at_k(b_attempts)
        c_res = resolve_at_k(c_attempts)
        if c_res and not b_res:
            world_reset_wins += 1
        per_instance.append(
            {
                "instance_id": iid,
                "dirty_retry": resolve_at_k(by_inst_cond.get((iid, "dirty-retry"), [])),
                "clean_restart": b_res,
                "full_reset": c_res,
                "world_reset_win": c_res and not b_res,
            }
        )

    n = len(instance_ids)
    win_rate = world_reset_wins / n if n else 0.0
    go_rg = float(thresholds.get("recovery_gap_go_pp", 5.0))
    nogo_rg = float(thresholds.get("recovery_gap_nogo_pp", 3.0))
    min_wins = int(thresholds.get("world_reset_wins_min", 2))

    if rg_pp >= go_rg and world_reset_wins >= min_wins:
        recommendation = "Go"
    elif rg_pp < nogo_rg:
        recommendation = "No-Go"
    else:
        recommendation = "Hold"

    return PilotMetrics(
        n_instances=n,
        recovery_gap_pp=rg_pp,
        world_reset_wins=world_reset_wins,
        world_reset_win_rate=win_rate,
        recommendation=recommendation,
        thresholds=thresholds,
        by_condition={k: v for k, v in by_condition.items()},
        per_instance=per_instance,
        warnings=warnings or [],
    )


def metrics_to_dict(m: PilotMetrics) -> dict:
    return {
        "n_instances": m.n_instances,
        "recovery_gap_pp": round(m.recovery_gap_pp, 2),
        "world_reset_wins": m.world_reset_wins,
        "world_reset_win_rate": round(m.world_reset_win_rate, 3),
        "recommendation": m.recommendation,
        "thresholds": m.thresholds,
        "warnings": m.warnings,
        "by_condition": {k: asdict(v) for k, v in m.by_condition.items()},
        "per_instance": m.per_instance,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Analyze dual-state contamination pilot metrics")
    parser.add_argument("--config", type=Path, default=SCRIPT_DIR / "config.yaml")
    parser.add_argument("--run-log", type=Path, help="Override run_log.jsonl path")
    parser.add_argument("--output", type=Path, help="Write metrics JSON path")
    parser.add_argument("--allow-mock", action="store_true", help="Allow mock rows for pipeline testing")
    parser.add_argument("--allow-unvalidated", action="store_true", help="Analyze real rows before hook validation")
    args = parser.parse_args()

    with args.config.open(encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    run_log = args.run_log or (REPO_ROOT / cfg["paths"]["run_log"]).resolve()
    metrics_out = args.output or (REPO_ROOT / cfg["paths"]["metrics"] / "pilot_summary.json").resolve()

    rows = load_jsonl(run_log)
    if not rows:
        print(f"No records in {run_log}. Run: python run_pilot.py --mock")
        return 1

    try:
        warnings = validate_rows(rows, cfg, allow_mock=args.allow_mock, allow_unvalidated=args.allow_unvalidated)
    except ValueError as exc:
        print(str(exc))
        return 1

    result = analyze_rows(rows, cfg["thresholds"], warnings)
    payload = metrics_to_dict(result)
    metrics_out.parent.mkdir(parents=True, exist_ok=True)
    metrics_out.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"Instances: {result.n_instances}")
    print(f"Recovery Gap (clean-restart - dirty-retry): {result.recovery_gap_pp:.2f} pp")
    print(f"World-reset wins (C resolved, B not): {result.world_reset_wins}/{result.n_instances}")
    print(f"Recommendation: {result.recommendation}")
    for warning in result.warnings:
        print(f"Warning: {warning}")
    print(f"Wrote {metrics_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
