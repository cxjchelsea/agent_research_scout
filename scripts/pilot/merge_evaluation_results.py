#!/usr/bin/env python3
"""Merge SWE-bench evaluation resolved labels into run_log.jsonl.

Accepted input formats:

1. JSON object mapping instance_id -> bool
2. JSON object mapping instance_id -> {"resolved": bool}
3. JSON list of objects with instance_id and resolved/is_resolved/success

The merge updates all rows for the matching instance. If you evaluate each
attempt separately, include attempt and condition fields in the evaluation rows.
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


def load_results(path: Path) -> dict[tuple[str, str | None, int | None], bool]:
    data = json.loads(path.read_text(encoding="utf-8"))
    results: dict[tuple[str, str | None, int | None], bool] = {}

    if isinstance(data, dict):
        for instance_id, value in data.items():
            resolved = extract_bool(value)
            if resolved is not None:
                condition = value.get("condition") if isinstance(value, dict) else None
                attempt = value.get("attempt") if isinstance(value, dict) else None
                results[(instance_id, condition, attempt)] = resolved
    elif isinstance(data, list):
        for item in data:
            if not isinstance(item, dict) or "instance_id" not in item:
                continue
            resolved = extract_bool(item)
            if resolved is not None:
                results[(item["instance_id"], item.get("condition"), item.get("attempt"))] = resolved
    return results


def lookup(
    results: dict[tuple[str, str | None, int | None], bool],
    *,
    instance_id: str,
    condition: str,
    attempt: int,
) -> bool | None:
    for key in (
        (instance_id, condition, attempt),
        (instance_id, condition, None),
        (instance_id, None, attempt),
        (instance_id, None, None),
    ):
        if key in results:
            return results[key]
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description="Merge SWE-bench evaluation labels into pilot run_log")
    parser.add_argument("--config", type=Path, default=SCRIPT_DIR / "config.yaml")
    parser.add_argument("--results", type=Path, required=True, help="Evaluation JSON file")
    parser.add_argument("--run-log", type=Path, help="Override run_log.jsonl path")
    parser.add_argument("--output", type=Path, help="Output run_log path; defaults to in-place")
    args = parser.parse_args()

    with args.config.open(encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    run_log = args.run_log or (REPO_ROOT / cfg["paths"]["run_log"]).resolve()
    output = args.output or run_log
    rows = load_jsonl(run_log)
    results = load_results(args.results)

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
