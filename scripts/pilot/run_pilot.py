#!/usr/bin/env python3
"""
Orchestrate dual-state contamination pilot runs on SWE-bench Verified.

Wraps mini-SWE-agent (external) with three retry conditions:
  A dirty-retry | B clean-restart | C full-reset

Usage:
  python run_pilot.py --dry-run              # print commands only
  python run_pilot.py --smoke-test           # run one mini-SWE-agent command with --exit-immediately
  python run_pilot.py --execute              # run full mini-SWE-agent commands
  python run_pilot.py --mock                 # write placeholder trajectories (for pipeline test)
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import random
import shutil
import shlex
import subprocess
import sys
from pathlib import Path

import yaml

from conditions import get_condition
from trajectory_schema import AttemptRecord, append_jsonl

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[1]


def configure_utf8_stdio() -> None:
    """Reduce Windows GBK console failures from mini-SWE-agent/Rich output."""
    os.environ.setdefault("PYTHONUTF8", "1")
    os.environ.setdefault("PYTHONIOENCODING", "utf-8")
    os.environ.setdefault("PYTHONLEGACYWINDOWSSTDIO", "0")
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            try:
                stream.reconfigure(encoding="utf-8", errors="replace")
            except Exception:
                pass


def load_env_file(path: Path) -> None:
    """Load KEY=VALUE pairs from a local .env file without overriding shell env."""
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key:
            os.environ.setdefault(key, value)


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
    smoke_test: bool = False,
) -> list[str]:
    msa = cfg["mini_swe_agent"]
    output_path = trajectory_output_path(output_dir, instance_id, condition_id, attempt)
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
        str(output_path),
        "--environment-class",
        msa.get("environment_class", "docker"),
        "--agent-class",
        "default",
    ]
    if msa.get("config"):
        cmd.extend(["-c", msa["config"]])
    cmd.extend(msa.get("extra_args") or [])
    if smoke_test:
        cmd.extend(msa.get("smoke_extra_args") or [])
    return cmd


def trajectory_output_path(output_dir: Path, instance_id: str, condition_id: str, attempt: int) -> Path:
    return output_dir / f"{instance_id}__{condition_id}__a{attempt}.json"


def pseudo_workspace_hash(instance_id: str, condition_id: str, attempt: int, resolved: bool) -> str:
    raw = f"{instance_id}|{condition_id}|{attempt}|{resolved}"
    return hashlib.sha256(raw.encode()).hexdigest()[:16]


def find_bool_key(data: object, keys: set[str]) -> bool | None:
    if isinstance(data, dict):
        for key, value in data.items():
            if key in keys and isinstance(value, bool):
                return value
        for value in data.values():
            found = find_bool_key(value, keys)
            if found is not None:
                return found
    elif isinstance(data, list):
        for value in data:
            found = find_bool_key(value, keys)
            if found is not None:
                return found
    return None


def parse_resolved_from_trajectory(path: Path) -> bool | None:
    """Best-effort parser; SWE-bench evaluation remains the source of truth."""
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    return find_bool_key(data, {"resolved", "is_resolved", "success", "passed"})


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
        run_mode="mock",
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
    proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    output = (proc.stdout or "") + (proc.stderr or "")
    return proc.returncode, output


def main() -> int:
    load_env_file(REPO_ROOT / ".env")
    load_env_file(SCRIPT_DIR / ".env")

    parser = argparse.ArgumentParser(description="Run dual-state contamination pilot")
    parser.add_argument("--config", type=Path, default=SCRIPT_DIR / "config.yaml")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dry-run", action="store_true", help="Print full-run mini-swe-agent commands only")
    mode.add_argument("--smoke-test", action="store_true", help="Run one infra smoke test with --exit-immediately")
    mode.add_argument("--execute", action="store_true", help="Execute full mini-swe-agent run (requires Docker + API key)")
    mode.add_argument("--mock", action="store_true", help="Write synthetic trajectories for pipeline testing")
    parser.add_argument("--model", default=os.environ.get("MINI_SWE_MODEL"))
    parser.add_argument("--instances", type=Path, help="Override instances.json path")
    parser.add_argument("--only-condition", choices=["dirty-retry", "clean-restart", "full-reset"])
    parser.add_argument("--only-instance", help="Run a single instance id")
    parser.add_argument("--reset-log", action="store_true", help="Delete existing run_log.jsonl before writing")
    parser.add_argument("--backend", choices=["cli", "python-api"], help="Execution backend for --execute")
    args = parser.parse_args()

    cfg = load_config(args.config)
    repo_root = REPO_ROOT
    paths = cfg["paths"]
    instances_path = args.instances or resolve_path(repo_root, paths["instances"])
    trajectories_dir = resolve_path(repo_root, paths["trajectories"])
    predictions_dir = resolve_path(repo_root, paths.get("predictions", "outputs/pilot/predictions"))
    run_log = resolve_path(repo_root, paths["run_log"])

    if not instances_path.exists():
        print(f"Missing {instances_path}. Run: python sample_instances.py", file=sys.stderr)
        return 1

    instance_ids = load_instances(instances_path)
    if args.only_instance:
        instance_ids = [args.only_instance]
    elif args.smoke_test:
        instance_ids = instance_ids[:1]

    model = args.model or cfg["model"]["default"]
    conditions = [c["id"] for c in cfg["conditions"]]
    if args.only_condition:
        conditions = [args.only_condition]
    elif args.smoke_test:
        conditions = ["dirty-retry"]
    max_attempts = int(cfg["pilot"]["max_attempts"])
    if args.smoke_test:
        max_attempts = 1
    seed = int(cfg["pilot"]["seed"])
    rng = random.Random(seed)

    trajectories_dir.mkdir(parents=True, exist_ok=True)
    if args.reset_log and run_log.exists():
        run_log.unlink()
    if args.reset_log and predictions_dir.exists():
        shutil.rmtree(predictions_dir)

    backend = args.backend or cfg.get("pilot", {}).get("backend", "cli")
    if args.execute and backend == "python-api":
        from backend.mini_swe_adapter import MiniSweDependencyError, MiniSwePythonBackend

        try:
            MiniSwePythonBackend(
                cfg=cfg,
                model=model,
                trajectories_dir=trajectories_dir,
                predictions_dir=predictions_dir,
                run_log=run_log,
            ).run(instance_ids=instance_ids, condition_ids=conditions, max_attempts=max_attempts)
        except MiniSweDependencyError as exc:
            print(str(exc), file=sys.stderr)
            return 1
        return 0

    for instance_id in instance_ids:
        for condition_id in conditions:
            cond = get_condition(condition_id)
            resolved_in_run = False
            for attempt in range(1, max_attempts + 1):
                if resolved_in_run:
                    break

                if args.mock:
                    record = mock_attempt(instance_id, condition_id, attempt, rng)
                    resolved_in_run = bool(record.resolved)
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
                    smoke_test=args.smoke_test,
                )
                trajectory_path = trajectory_output_path(out_dir, instance_id, condition_id, attempt)

                # Condition-specific env hints for manual mini-swe-agent hooks / fork
                env = os.environ.copy()
                env.setdefault("PYTHONUTF8", "1")
                env.setdefault("PYTHONIOENCODING", "utf-8")
                env.setdefault("PYTHONLEGACYWINDOWSSTDIO", "0")
                env["PILOT_CONDITION"] = condition_id
                env["PILOT_CONTEXT_POLICY"] = cond.context_policy.value
                env["PILOT_WORLD_POLICY"] = cond.world_policy.value
                env["PILOT_ATTEMPT"] = str(attempt)

                if args.dry_run:
                    print(f"# {instance_id} {condition_id} attempt {attempt}")
                    print(f"# PILOT_CONTEXT_POLICY={cond.context_policy.value} PILOT_WORLD_POLICY={cond.world_policy.value}")
                    run_single_command(cmd, dry_run=True)
                    continue

                if args.smoke_test:
                    proc = subprocess.run(
                        cmd,
                        env=env,
                        capture_output=True,
                        text=True,
                        encoding="utf-8",
                        errors="replace",
                    )
                    print(f"[smoke] {instance_id} {condition_id} a{attempt} exit={proc.returncode}")
                    if proc.stdout:
                        print(proc.stdout[-2000:])
                    if proc.stderr:
                        print(proc.stderr[-2000:], file=sys.stderr)
                    return proc.returncode

                if args.execute:
                    printable = " ".join(shlex.quote(c) for c in cmd)
                    proc = subprocess.run(
                        cmd,
                        env=env,
                        capture_output=True,
                        text=True,
                        encoding="utf-8",
                        errors="replace",
                    )
                    output = (proc.stdout or "") + (proc.stderr or "")
                    resolved = parse_resolved_from_trajectory(trajectory_path)
                    error_parts = []
                    if proc.returncode != 0:
                        error_parts.append(f"exit_code={proc.returncode}")
                    if resolved is None:
                        error_parts.append("resolved_unparsed")
                    record = AttemptRecord(
                        instance_id=instance_id,
                        condition=condition_id,
                        attempt=attempt,
                        resolved=resolved,
                        run_mode="execute",
                        trajectory_path=str(trajectory_path),
                        mini_swe_output=output[-4000:] if output else None,
                        error=";".join(error_parts) if error_parts else None,
                    )
                    append_jsonl(run_log, record)
                    print(f"[run] {instance_id} {condition_id} a{attempt} exit={proc.returncode} resolved={resolved}")
                    if resolved:
                        resolved_in_run = True

    if args.mock:
        print(f"\nMock trajectories appended to {run_log}")
        print("Next: python analyze_pilot.py")
    elif args.dry_run:
        print("\nDry-run complete. Use --smoke-test for infra check, then --execute for real runs.")
    return 0


if __name__ == "__main__":
    configure_utf8_stdio()
    raise SystemExit(main())
