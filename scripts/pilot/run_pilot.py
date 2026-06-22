#!/usr/bin/env python3
"""
Orchestrate dual-state contamination pilot runs on SWE-bench Verified.

Wraps mini-SWE-agent (external) with three retry conditions:
  A dirty-retry | B clean-restart | C full-reset

Usage:
  python run_pilot.py --dry-run              # print commands only
  python run_pilot.py --execute              # run via mini-extra swebench-single
  python run_pilot.py --mock                 # write placeholder trajectories (for pipeline test)
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import random
import shlex
import subprocess
import sys
from pathlib import Path

import yaml

from conditions import get_condition
from trajectory_schema import AttemptRecord, append_jsonl, load_jsonl

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[1]


def load_config(config_path: Path) -> dict:
    with config_path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_instances(path: Path) -> list[str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return list(data["instance_ids"])


def resolve_path(repo_root: Path, rel: str) -> Path:
    return (repo_root / rel).resolve()


def build_mini_command(
    cfg: dict,
    *,
    instance_id: str,
    condition_id: str,
    attempt: int,
    output_dir: Path,
    model: str,
) -> list[str]:
    msa = cfg["mini_swe_agent"]
    cmd = [
        msa.get("command", "mini-extra"),
        msa.get("subcommand", "swebench-single"),
        "--subset",
        msa.get("subset", "verified"),
        "--split",
        msa.get("split", "test"),
        "-i",
        instance_id,
        "-m",
        model,
        "-o",
        str(output_dir / f"{instance_id}__{condition_id}__a{attempt}.json"),
        "--environment-class",
        msa.get("environment_class", "docker"),
        "--exit-immediately",
    ]
    if msa.get("config"):
        cmd.extend(["-c", msa["config"]])
    cmd.extend(msa.get("extra_args") or [])
    return cmd


def pseudo_workspace_hash(instance_id: str, condition_id: str, attempt: int, resolved: bool) -> str:
    raw = f"{instance_id}|{condition_id}|{attempt}|{resolved}"
    return hashlib.sha256(raw.encode()).hexdigest()[:16]


def mock_attempt(
    instance_id: str,
    condition_id: str,
    attempt: int,
    rng: random.Random,
) -> AttemptRecord:
    """Generate synthetic attempt for testing analyze_pilot without Docker."""
    cond = get_condition(condition_id)
    base_resolve_p = {"dirty-retry": 0.15, "clean-restart": 0.22, "full-reset": 0.28}[condition_id]
    resolve_p = min(0.95, base_resolve_p + 0.05 * (attempt - 1))
    resolved = rng.random() < resolve_p
    initial_hash = pseudo_workspace_hash(instance_id, "initial", 0, False)
    workspace_hash = pseudo_workspace_hash(instance_id, condition_id, attempt, resolved)
    first_step_error = rng.random() < (0.4 if attempt > 1 and cond.context_policy.value == "retain" else 0.2)
    return AttemptRecord(
        instance_id=instance_id,
        condition=condition_id,
        attempt=attempt,
        resolved=resolved,
        first_step_error=first_step_error,
        workspace_hash=workspace_hash,
        initial_workspace_hash=initial_hash,
        context_token_count=int(rng.uniform(800, 12000) * (attempt if cond.context_policy.value == "retain" else 1)),
        trajectory_path=f"trajectories/{instance_id}__{condition_id}__a{attempt}.json",
        error=None if resolved or rng.random() > 0.1 else "mock_timeout",
    )


def run_single_command(cmd: list[str], dry_run: bool) -> tuple[int, str]:
    printable = " ".join(shlex.quote(c) for c in cmd)
    if dry_run:
        print(printable)
        return 0, printable
    proc = subprocess.run(cmd, capture_output=True, text=True)
    output = (proc.stdout or "") + (proc.stderr or "")
    return proc.returncode, output


def main() -> int:
    parser = argparse.ArgumentParser(description="Run dual-state contamination pilot")
    parser.add_argument("--config", type=Path, default=SCRIPT_DIR / "config.yaml")
    parser.add_argument("--dry-run", action="store_true", help="Print mini-swe-agent commands only")
    parser.add_argument("--execute", action="store_true", help="Execute mini-swe-agent (requires Docker + API key)")
    parser.add_argument("--mock", action="store_true", help="Write synthetic trajectories for pipeline testing")
    parser.add_argument("--model", default=os.environ.get("MINI_SWE_MODEL"))
    parser.add_argument("--instances", type=Path, help="Override instances.json path")
    parser.add_argument("--only-condition", choices=["dirty-retry", "clean-restart", "full-reset"])
    parser.add_argument("--only-instance", help="Run a single instance id")
    args = parser.parse_args()

    if not args.dry_run and not args.execute and not args.mock:
        parser.error("Specify one of --dry-run, --execute, or --mock")

    cfg = load_config(args.config)
    repo_root = REPO_ROOT
    paths = cfg["paths"]
    instances_path = args.instances or resolve_path(repo_root, paths["instances"])
    trajectories_dir = resolve_path(repo_root, paths["trajectories"])
    run_log = resolve_path(repo_root, paths["run_log"])

    if not instances_path.exists():
        print(f"Missing {instances_path}. Run: python sample_instances.py", file=sys.stderr)
        return 1

    instance_ids = load_instances(instances_path)
    if args.only_instance:
        instance_ids = [args.only_instance]

    model = args.model or cfg["model"]["default"]
    conditions = [c["id"] for c in cfg["conditions"]]
    if args.only_condition:
        conditions = [args.only_condition]
    max_attempts = int(cfg["pilot"]["max_attempts"])
    seed = int(cfg["pilot"]["seed"])
    rng = random.Random(seed)

    trajectories_dir.mkdir(parents=True, exist_ok=True)

    for instance_id in instance_ids:
        for condition_id in conditions:
            cond = get_condition(condition_id)
            resolved_in_run = False
            for attempt in range(1, max_attempts + 1):
                if resolved_in_run:
                    break

                if args.mock:
                    record = mock_attempt(instance_id, condition_id, attempt, rng)
                    resolved_in_run = record.resolved
                    append_jsonl(run_log, record)
                    print(f"[mock] {instance_id} {condition_id} a{attempt} resolved={record.resolved}")
                    continue

                out_dir = trajectories_dir / instance_id / condition_id
                out_dir.mkdir(parents=True, exist_ok=True)
                cmd = build_mini_command(
                    cfg,
                    instance_id=instance_id,
                    condition_id=condition_id,
                    attempt=attempt,
                    output_dir=out_dir,
                    model=model,
                )

                # Condition-specific env hints for manual mini-swe-agent hooks / fork
                env = os.environ.copy()
                env["PILOT_CONDITION"] = condition_id
                env["PILOT_CONTEXT_POLICY"] = cond.context_policy.value
                env["PILOT_WORLD_POLICY"] = cond.world_policy.value
                env["PILOT_ATTEMPT"] = str(attempt)

                if args.dry_run:
                    print(f"# {instance_id} {condition_id} attempt {attempt}")
                    print(f"# PILOT_CONTEXT_POLICY={cond.context_policy.value} PILOT_WORLD_POLICY={cond.world_policy.value}")
                    run_single_command(cmd, dry_run=True)
                    continue

                if args.execute:
                    printable = " ".join(shlex.quote(c) for c in cmd)
                    proc = subprocess.run(cmd, env=env, capture_output=True, text=True)
                    output = (proc.stdout or "") + (proc.stderr or "")
                    resolved = proc.returncode == 0  # placeholder; parse trajectory for real resolve
                    record = AttemptRecord(
                        instance_id=instance_id,
                        condition=condition_id,
                        attempt=attempt,
                        resolved=resolved,
                        trajectory_path=str(out_dir / f"{instance_id}__{condition_id}__a{attempt}.json"),
                        mini_swe_output=output[-4000:] if output else None,
                        error=None if proc.returncode == 0 else f"exit_code={proc.returncode}",
                    )
                    append_jsonl(run_log, record)
                    print(f"[run] {instance_id} {condition_id} a{attempt} exit={proc.returncode}")
                    if resolved:
                        resolved_in_run = True

    if args.mock:
        print(f"\nMock trajectories appended to {run_log}")
        print("Next: python analyze_pilot.py")
    elif args.dry_run:
        print("\nDry-run complete. Install mini-swe-agent + Docker, set MINI_SWE_MODEL / API keys, then --execute.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
