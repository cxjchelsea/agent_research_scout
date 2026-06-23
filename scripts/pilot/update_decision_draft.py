#!/usr/bin/env python3
"""Generate decision update draft from pilot metrics (manual merge into decision.md)."""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[1]
DECISION_PATH = REPO_ROOT / "topics" / "state_contamination" / "decision.md"
METRICS_DEFAULT = REPO_ROOT / "outputs" / "pilot" / "metrics" / "pilot_summary.json"


def main() -> int:
    parser = argparse.ArgumentParser(description="Draft decision update from pilot metrics")
    parser.add_argument("--metrics", type=Path, default=METRICS_DEFAULT)
    parser.add_argument("-o", "--output", type=Path, default=REPO_ROOT / "outputs" / "pilot" / "decision_draft.md")
    args = parser.parse_args()

    if not args.metrics.exists():
        print(f"Missing {args.metrics}. Run analyze_pilot.py first.")
        return 1

    m = json.loads(args.metrics.read_text(encoding="utf-8"))
    rec = m["recommendation"]
    evidence_level = m.get("evidence_level", "unknown")
    rg = m["recovery_gap_pp"]
    wins = m["world_reset_wins"]
    n = m["n_instances"]

    if evidence_level == "infrastructure":
        decision = "Hold"
        reason = (
            f"Infrastructure pilot only (n={n}). RG={rg:.2f}pp and world-reset wins={wins}/{n} "
            "can guide whether to scale, but must not be treated as paper-level Go evidence."
        )
    elif rec == "Go":
        decision = "Go"
        reason = f"Pilot RG={rg:.2f}pp (>=5), world-reset wins={wins}/{n} (>=2)."
    elif rec == "No-Go":
        decision = "No-Go"
        reason = f"Pilot RG={rg:.2f}pp (<3); dual-state eval lacks incremental signal."
    else:
        decision = "Hold"
        reason = f"Pilot RG={rg:.2f}pp in [3,5); expand sample or refine protocol."

    draft = f"""# Decision Draft (auto-generated — merge into decision.md)

> Generated: {date.today().isoformat()}
> Source: `{args.metrics.as_posix()}`

## Proposed Decision: **{decision}**

{reason}

## Pilot metrics snapshot

| Metric | Value | Threshold |
|--------|-------|-----------|
| Recovery Gap | {rg:.2f} pp | Go >= 5 pp |
| World-reset wins | {wins}/{n} | Go >= 2/{n} |
| Evidence level | {evidence_level} | infrastructure / signal / paper |
| Recommendation | {rec} | — |

## Manual steps after merge

1. Update `topics/state_contamination/decision.md` Decision + Reason tables
2. Re-run `topics/state_contamination/file_consistency_check.md`
3. If infrastructure-level Hold: scale to 20–30 instances before claiming Go
4. If Go at signal/paper level: extend experiment_plan to 50–100 instances
"""
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(draft, encoding="utf-8")
    print(draft)
    print(f"\nWrote draft to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
