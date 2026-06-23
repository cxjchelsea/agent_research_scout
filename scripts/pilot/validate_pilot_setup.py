#!/usr/bin/env python3
"""Validate that the pilot pipeline is ready for real experimental analysis.

This script intentionally separates two levels:

1. Static readiness: config files, instance sample, and condition definitions exist.
2. Evidence readiness: a run_log from real execution has no mock rows, has parsed
   resolved labels, and includes the fields required by CR/WSD metrics.

It cannot magically prove mini-SWE-agent implements the reset hook; that must be
verified by a smoke run or fork-specific test, then recorded by setting
state_control.hook_validated=true in config.yaml.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

import yaml

from conditions import CONDITIONS
from trajectory_schema import load_jsonl

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[1]


def repo_path(cfg: dict, key: str) -> Path:
    return (REPO_ROOT / cfg["paths"][key]).resolve()


def status_line(ok: bool, message: str) -> str:
    return f"[{'PASS' if ok else 'FAIL'}] {message}"


def check_static(cfg: dict) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    condition_ids = [item["id"] for item in cfg.get("conditions", [])]
    expected = set(CONDITIONS)
    if set(condition_ids) != expected:
        errors.append(f"conditions mismatch: expected {sorted(expected)}, got {condition_ids}")

    policies = {item["id"]: (item["context_policy"], item["world_policy"]) for item in cfg.get("conditions", [])}
    expected_policies = {
        "dirty-retry": ("retain", "retain"),
        "clean-restart": ("reset", "retain"),
        "full-reset": ("reset", "reset"),
    }
    for condition, expected_policy in expected_policies.items():
        if policies.get(condition) != expected_policy:
            errors.append(f"{condition} policy should be {expected_policy}, got {policies.get(condition)}")

    msa = cfg.get("mini_swe_agent") or {}
    backend = (cfg.get("pilot") or {}).get("backend", "cli")
    if backend not in {"cli", "python-api"}:
        errors.append(f"unknown pilot.backend: {backend}")
    if backend == "cli":
        warnings.append("pilot.backend=cli cannot enforce context/workspace reset without an external mini-SWE-agent hook")
    if backend == "python-api":
        adapter_path = SCRIPT_DIR / "backend" / "mini_swe_adapter.py"
        if not adapter_path.exists():
            errors.append("pilot.backend=python-api but backend/mini_swe_adapter.py is missing")

    if "--exit-immediately" in (msa.get("extra_args") or []):
        errors.append("--exit-immediately must not be in mini_swe_agent.extra_args for real --execute")
    if "--exit-immediately" not in (msa.get("smoke_extra_args") or []):
        warnings.append("--exit-immediately is not configured for --smoke-test")

    instances_path = repo_path(cfg, "instances")
    if not instances_path.exists():
        errors.append(f"missing instances file: {instances_path}")
    else:
        data = json.loads(instances_path.read_text(encoding="utf-8"))
        if len(data.get("instance_ids", [])) != int(cfg["pilot"]["n_instances"]):
            warnings.append("instances.json count differs from config pilot.n_instances")

    return errors, warnings


def check_run_log(cfg: dict, *, allow_mock: bool) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    run_log = repo_path(cfg, "run_log")
    rows = load_jsonl(run_log)

    if not rows:
        warnings.append(f"no run_log rows found at {run_log}; static validation only")
        return errors, warnings

    modes = {row.get("run_mode", "unknown") for row in rows}
    if "mock" in modes and not allow_mock:
        errors.append("run_log contains mock rows; delete run_log or pass --allow-mock for pipeline tests")

    by_inst_cond: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for row in rows:
        by_inst_cond[(row.get("instance_id"), row.get("condition"))].append(row)

    instance_ids = sorted({row.get("instance_id") for row in rows})
    for instance_id in instance_ids:
        for condition in CONDITIONS:
            if (instance_id, condition) not in by_inst_cond:
                warnings.append(f"{instance_id} missing condition {condition}")

    missing_resolved = [row for row in rows if row.get("resolved") is None]
    if missing_resolved:
        errors.append(f"{len(missing_resolved)} rows have resolved=null")

    missing_first_step = [row for row in rows if row.get("first_step_error") is None]
    if missing_first_step:
        warnings.append(f"{len(missing_first_step)} rows lack first_step_error; CR incomplete")

    missing_hash = [
        row for row in rows if not row.get("workspace_hash") or not row.get("initial_workspace_hash")
    ]
    if missing_hash:
        warnings.append(f"{len(missing_hash)} rows lack workspace hashes; WSD incomplete")

    return errors, warnings


def run_dry_command() -> tuple[bool, str]:
    proc = subprocess.run(
        [sys.executable, "run_pilot.py", "--dry-run", "--only-instance", "dummy__dummy-1", "--only-condition", "dirty-retry"],
        cwd=SCRIPT_DIR,
        capture_output=True,
        text=True,
    )
    output = (proc.stdout or "") + (proc.stderr or "")
    return proc.returncode == 0 and "--exit-immediately" not in output, output[-1000:]


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate dual-state pilot setup")
    parser.add_argument("--config", type=Path, default=SCRIPT_DIR / "config.yaml")
    parser.add_argument("--allow-mock", action="store_true", help="Allow mock run_log rows for pipeline testing")
    args = parser.parse_args()

    with args.config.open(encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    errors, warnings = check_static(cfg)
    log_errors, log_warnings = check_run_log(cfg, allow_mock=args.allow_mock)
    errors.extend(log_errors)
    warnings.extend(log_warnings)

    dry_ok, dry_tail = run_dry_command()
    if not dry_ok:
        errors.append("--dry-run either failed or included --exit-immediately")
        warnings.append(f"dry-run output tail: {dry_tail}")

    hook_validated = bool((cfg.get("state_control") or {}).get("hook_validated"))
    if not hook_validated:
        warnings.append("state_control.hook_validated=false; real pilot results must not update decision yet")

    print(status_line(not errors, "pilot setup validation"))
    for warning in warnings:
        print(f"[WARN] {warning}")
    for error in errors:
        print(f"[FAIL] {error}")

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
