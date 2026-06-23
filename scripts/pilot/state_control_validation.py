#!/usr/bin/env python3
"""Validate observable state-control evidence in pilot run_log.jsonl.

This script checks the experimental contract behind the three conditions:

- dirty-retry / clean-restart retain workspace state across attempts.
- full-reset starts each attempt from a fresh workspace snapshot.
- dirty-retry should retain context evidence, while clean/full reset should not.

Workspace checks use pre/post hashes recorded by the Python backend. Context
checks require context_token_count or an equivalent future field; if missing,
the script fails unless --world-only is passed.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from pathlib import Path

import yaml

from trajectory_schema import load_jsonl

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[1]


def repo_path(cfg: dict, key: str) -> Path:
    return (REPO_ROOT / cfg["paths"][key]).resolve()


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def validate_world(rows: list[dict]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    by_inst_cond: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for row in rows:
        by_inst_cond[(row.get("instance_id"), row.get("condition"))].append(row)

    for (instance_id, condition), attempts in sorted(by_inst_cond.items()):
        attempts = sorted(attempts, key=lambda row: int(row.get("attempt", 0)))
        previous_post_hash = None
        for row in attempts:
            attempt = int(row.get("attempt", 0))
            pre_hash = row.get("pre_attempt_workspace_hash")
            post_hash = row.get("workspace_hash")
            initial_hash = row.get("initial_workspace_hash")
            label = f"{instance_id} {condition} a{attempt}"

            if not pre_hash or not post_hash or not initial_hash:
                fail(errors, f"{label}: missing initial/pre/post workspace hashes")
                previous_post_hash = post_hash
                continue

            if attempt == 1 and pre_hash != initial_hash:
                fail(errors, f"{label}: attempt1 pre hash differs from initial hash")

            if attempt > 1 and condition in {"dirty-retry", "clean-restart"}:
                if not previous_post_hash:
                    fail(errors, f"{label}: missing previous post hash for retained-world check")
                elif pre_hash != previous_post_hash:
                    fail(errors, f"{label}: retained-world pre hash does not match previous post hash")

            if attempt > 1 and condition == "full-reset" and pre_hash != initial_hash:
                fail(errors, f"{label}: full-reset pre hash differs from fresh initial hash")

            if condition in {"dirty-retry", "clean-restart"} and attempt > 1 and pre_hash == initial_hash:
                warnings.append(f"{label}: retained workspace is unchanged; sentinel/diff evidence may be weak")

            previous_post_hash = post_hash

    return errors, warnings


def validate_context(rows: list[dict]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    by_inst_cond: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for row in rows:
        by_inst_cond[(row.get("instance_id"), row.get("condition"))].append(row)

    for (instance_id, condition), attempts in sorted(by_inst_cond.items()):
        attempts = sorted(attempts, key=lambda row: int(row.get("attempt", 0)))
        token_counts = [row.get("context_token_count") for row in attempts]
        label = f"{instance_id} {condition}"

        if any(count is None for count in token_counts):
            fail(errors, f"{label}: missing context_token_count; cannot validate context retain/reset")
            continue

        numeric_counts = [int(count) for count in token_counts]
        if condition == "dirty-retry":
            for prev, current in zip(numeric_counts, numeric_counts[1:]):
                if current < prev:
                    fail(errors, f"{label}: dirty-retry context_token_count decreased across attempts")
        else:
            # A reset context should not show monotonic accumulation across all retries.
            if len(numeric_counts) > 1 and all(current > prev for prev, current in zip(numeric_counts, numeric_counts[1:])):
                warnings.append(f"{label}: reset condition token counts monotonically increased; inspect trajectories")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate pilot state-control evidence")
    parser.add_argument("--config", type=Path, default=SCRIPT_DIR / "config.yaml")
    parser.add_argument("--run-log", type=Path, help="Override run_log.jsonl path")
    parser.add_argument("--world-only", action="store_true", help="Validate workspace reset/retain only")
    args = parser.parse_args()

    with args.config.open(encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    run_log = args.run_log or repo_path(cfg, "run_log")
    rows = load_jsonl(run_log)
    if not rows:
        print(f"[FAIL] no rows in {run_log}")
        return 1

    errors, warnings = validate_world(rows)
    if args.world_only:
        warnings.append("world-only mode: context retain/reset still requires manual or token-count validation")
    else:
        context_errors, context_warnings = validate_context(rows)
        errors.extend(context_errors)
        warnings.extend(context_warnings)

    print(f"[{'PASS' if not errors else 'FAIL'}] state-control validation")
    for warning in warnings:
        print(f"[WARN] {warning}")
    for error in errors:
        print(f"[FAIL] {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
