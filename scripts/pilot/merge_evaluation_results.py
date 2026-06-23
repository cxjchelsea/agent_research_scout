#!/usr/bin/env python3
"""Merge SWE-bench evaluation resolved labels into run_log.jsonl.

The pilot runs the same instance under multiple conditions and attempts, so a
resolved label is only safe to merge when it is keyed by:

    instance_id + condition + attempt

If an evaluation output only contains instance_id -> resolved, pass
--condition and --attempt for the prediction file being merged. Otherwise the
script refuses to merge instead of silently copying one result to unrelated
conditions/attempts.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import yaml

from trajectory_schema import load_jsonl

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[1]


def extract_bool(value: Any) -> bool | None:
    if isinstance(value, bool):
        return value
    if isinstance(value, dict):
        for key in ("resolved", "is_resolved", "success", "passed"):
            if isinstance(value.get(key), bool):
                return value[key]
    return None


def coerce_attempt(value: Any) -> int | None:
    if value is None:
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def get_condition(item: dict[str, Any]) -> str | None:
    value = item.get("condition", item.get("pilot_condition"))
    return str(value) if value is not None else None


def get_attempt(item: dict[str, Any]) -> int | None:
    return coerce_attempt(item.get("attempt", item.get("pilot_attempt")))


def add_result(
    results: dict[tuple[str, str, int], bool],
    *,
    instance_id: str,
    condition: str | None,
    attempt: int | None,
    resolved: bool,
    errors: list[str],
) -> None:
    if not condition or attempt is None:
        errors.append(
            f"{instance_id}: missing condition/attempt; pass --condition and --attempt "
            "or include condition+attempt in the evaluation row"
        )
        return
    key = (instance_id, condition, attempt)
    if key in results:
        errors.append(f"duplicate evaluation result for {key}")
        return
    results[key] = resolved


def load_results(
    path: Path,
    *,
    condition_override: str | None,
    attempt_override: int | None,
) -> dict[tuple[str, str, int], bool]:
    data = json.loads(path.read_text(encoding="utf-8"))
    results: dict[tuple[str, str, int], bool] = {}
    errors: list[str] = []

    if isinstance(data, dict):
        for instance_id, value in data.items():
            resolved = extract_bool(value)
            if resolved is not None:
                condition = condition_override
                attempt = attempt_override
                if isinstance(value, dict):
                    condition = get_condition(value) or condition
                    attempt = get_attempt(value) if get_attempt(value) is not None else attempt
                add_result(
                    results,
                    instance_id=str(instance_id),
                    condition=condition,
                    attempt=attempt,
                    resolved=resolved,
                    errors=errors,
                )
    elif isinstance(data, list):
        for item in data:
            if not isinstance(item, dict) or "instance_id" not in item:
                continue
            resolved = extract_bool(item)
            if resolved is not None:
                add_result(
                    results,
                    instance_id=str(item["instance_id"]),
                    condition=get_condition(item) or condition_override,
                    attempt=get_attempt(item) if get_attempt(item) is not None else attempt_override,
                    resolved=resolved,
                    errors=errors,
                )
    else:
        errors.append(f"unsupported evaluation result format in {path}")
    if errors:
        detail = "\n".join(f"- {error}" for error in errors[:20])
        raise ValueError(f"Unsafe evaluation merge input:\n{detail}")
    return results


def lookup(
    results: dict[tuple[str, str, int], bool],
    *,
    instance_id: str,
    condition: str,
    attempt: int,
) -> bool | None:
    return results.get((instance_id, condition, attempt))


def main() -> int:
    parser = argparse.ArgumentParser(description="Merge SWE-bench evaluation labels into pilot run_log")
    parser.add_argument("--config", type=Path, default=SCRIPT_DIR / "config.yaml")
    parser.add_argument("--results", type=Path, required=True, help="Evaluation JSON file")
    parser.add_argument("--run-log", type=Path, help="Override run_log.jsonl path")
    parser.add_argument("--output", type=Path, help="Output run_log path; defaults to in-place")
    parser.add_argument("--condition", choices=["dirty-retry", "clean-restart", "full-reset"], help="Condition for instance-only evaluation outputs")
    parser.add_argument("--attempt", type=int, help="Attempt number for instance-only evaluation outputs")
    args = parser.parse_args()

    if (args.condition is None) != (args.attempt is None):
        parser.error("--condition and --attempt must be provided together")

    with args.config.open(encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    run_log = args.run_log or (REPO_ROOT / cfg["paths"]["run_log"]).resolve()
    output = args.output or run_log
    rows = load_jsonl(run_log)
    try:
        results = load_results(args.results, condition_override=args.condition, attempt_override=args.attempt)
    except ValueError as exc:
        print(str(exc))
        return 1

    updated = 0
    for row in rows:
        resolved = lookup(
            results,
            instance_id=row["instance_id"],
            condition=row["condition"],
            attempt=int(row["attempt"]),
        )
        if resolved is not None:
            row["resolved"] = resolved
            if row.get("error") == "resolved_requires_swebench_evaluation":
                row["error"] = None
            updated += 1

    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    print(f"Updated {updated}/{len(rows)} rows in {output}")
    return 0 if updated else 1


if __name__ == "__main__":
    raise SystemExit(main())
