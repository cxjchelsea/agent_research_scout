#!/usr/bin/env python3
"""Sample SWE-bench Verified instances for the 10-question pilot."""

from __future__ import annotations

import argparse
import json
import random
from pathlib import Path

# Fallback IDs (SWE-bench Verified test split, commonly used in docs)
DEFAULT_VERIFIED_INSTANCES = [
    "django__django-11099",
    "sympy__sympy-15599",
    "matplotlib__matplotlib-18869",
    "scikit-learn__scikit-learn-10297",
    "astropy__astropy-12907",
    "pytest-dev__pytest-8906",
    "sphinx-doc__sphinx-8721",
    "pylint-dev__pylint-5859",
    "requests__requests-2315",
    "flask__flask-5063",
]


def load_verified_instance_ids() -> list[str]:
    try:
        from datasets import load_dataset  # type: ignore
    except ImportError:
        return DEFAULT_VERIFIED_INSTANCES.copy()

    ds = load_dataset("princeton-nlp/SWE-bench_Verified", split="test")
    return [row["instance_id"] for row in ds]


def sample_instances(n: int, seed: int) -> list[str]:
    pool = load_verified_instance_ids()
    rng = random.Random(seed)
    if n >= len(pool):
        return pool
    return rng.sample(pool, n)


def main() -> None:
    parser = argparse.ArgumentParser(description="Sample pilot instances for dual-state contamination")
    parser.add_argument("-n", "--count", type=int, default=10)
    parser.add_argument("-s", "--seed", type=int, default=42)
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path(__file__).resolve().parents[2] / "outputs" / "pilot" / "instances.json",
    )
    args = parser.parse_args()

    ids = sample_instances(args.count, args.seed)
    payload = {
        "benchmark": "swe-bench_verified",
        "split": "test",
        "seed": args.seed,
        "n_instances": len(ids),
        "instance_ids": ids,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(ids)} instances to {args.output}")


if __name__ == "__main__":
    main()
