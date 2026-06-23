"""mini-SWE-agent Python API backend for dual-state retry conditions.

The state semantics are controlled by object lifetime:

- dirty-retry: reuse the same environment and the same agent across attempts.
- clean-restart: reuse the same environment, create a fresh agent per attempt.
- full-reset: create a fresh environment and a fresh agent per attempt.

SWE-bench resolved labels are not computed here. This backend records submissions
and trajectories; resolved must be merged from SWE-bench evaluation output.
"""

from __future__ import annotations

import json
import os
import sys
import traceback
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from conditions import ContextPolicy, WorldPolicy, get_condition
from trajectory_schema import AttemptRecord, append_jsonl


class MiniSweDependencyError(RuntimeError):
    pass


def require_minisweagent() -> dict[str, Any]:
    os.environ.setdefault("PYTHONUTF8", "1")
    os.environ.setdefault("PYTHONIOENCODING", "utf-8")
    os.environ.setdefault("PYTHONLEGACYWINDOWSSTDIO", "0")
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            try:
                stream.reconfigure(encoding="utf-8", errors="replace")
            except Exception:
                pass

    try:
        from datasets import load_dataset
        from minisweagent.agents import get_agent
        from minisweagent.config import builtin_config_dir, get_config_from_spec
        from minisweagent.models import get_model
        from minisweagent.run.benchmarks.swebench import DATASET_MAPPING, get_sb_environment
        from minisweagent.utils.serialize import UNSET, recursive_merge
    except ImportError as exc:
        raise MiniSweDependencyError(
            "mini-SWE-agent backend requires: pip install mini-swe-agent datasets"
        ) from exc

    return {
        "load_dataset": load_dataset,
        "get_agent": get_agent,
        "builtin_config_dir": builtin_config_dir,
        "get_config_from_spec": get_config_from_spec,
        "get_model": get_model,
        "DATASET_MAPPING": DATASET_MAPPING,
        "get_sb_environment": get_sb_environment,
        "UNSET": UNSET,
        "recursive_merge": recursive_merge,
    }


@dataclass
class AttemptResult:
    record: AttemptRecord
    exit_status: str | None
    submission: str | None


class MiniSwePythonBackend:
    def __init__(
        self,
        *,
        cfg: dict,
        model: str,
        trajectories_dir: Path,
        predictions_dir: Path,
        run_log: Path,
    ) -> None:
        self.cfg = cfg
        self.model = model
        self.trajectories_dir = trajectories_dir
        self.predictions_dir = predictions_dir
        self.run_log = run_log
        self.mswe = require_minisweagent()
        self.base_config = self._build_base_config()

    def _build_base_config(self) -> dict:
        default_config = self.mswe["builtin_config_dir"] / "benchmarks" / "swebench.yaml"
        config_specs = [str(default_config)]
        if self.cfg.get("mini_swe_agent", {}).get("config"):
            config_specs = [self.cfg["mini_swe_agent"]["config"]]

        configs = [self.mswe["get_config_from_spec"](spec) for spec in config_specs]
        env_class = self.cfg.get("mini_swe_agent", {}).get("environment_class", "docker")
        configs.append(
            {
                "agent": {
                    "agent_class": "default",
                    "output_path": self.mswe["UNSET"],
                },
                "model": {"model_name": self.model},
                "environment": {"environment_class": env_class},
            }
        )
        return self.mswe["recursive_merge"](*configs)

    def load_instance(self, instance_id: str) -> dict:
        subset = self.cfg["mini_swe_agent"].get("subset", "verified")
        split = self.cfg["mini_swe_agent"].get("split", "test")
        dataset_path = self.mswe["DATASET_MAPPING"].get(subset, subset)
        dataset = self.mswe["load_dataset"](dataset_path, split=split)
        instances = {item["instance_id"]: item for item in dataset}
        if instance_id not in instances:
            raise KeyError(f"Instance not found in {dataset_path}/{split}: {instance_id}")
        return instances[instance_id]

    def make_env(self, instance: dict):
        return self.mswe["get_sb_environment"](dict(self.base_config), instance)

    def make_agent(self, env):
        model = self.mswe["get_model"](config=self.base_config.get("model", {}))
        return self.mswe["get_agent"](model, env, self.base_config.get("agent", {}), default_type="default")

    @staticmethod
    def workspace_hash(env) -> str | None:
        command = (
            "cd /testbed && "
            "{ find . -type f -not -path './.git/*' -print0 | sort -z | "
            "xargs -0 sha256sum 2>/dev/null || true; } | sha256sum | awk '{print $1}'"
        )
        try:
            out = env.execute({"command": command}, timeout=120)
        except Exception:
            return None
        if out.get("returncode") != 0:
            return None
        return (out.get("output") or "").strip().splitlines()[-1] if out.get("output") else None

    def save_agent(self, agent, path: Path, info: dict) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        if hasattr(agent, "save"):
            agent.save(path, info)
        else:
            path.write_text(json.dumps(info, indent=2, ensure_ascii=False), encoding="utf-8")

    def append_prediction(self, *, instance_id: str, condition_id: str, attempt: int, submission: str | None) -> Path:
        path = self.predictions_dir / f"{condition_id}__a{attempt}.jsonl"
        path.parent.mkdir(parents=True, exist_ok=True)
        row = {
            "model_name_or_path": self.model,
            "instance_id": instance_id,
            "model_patch": submission or "",
            "pilot_condition": condition_id,
            "pilot_attempt": attempt,
        }
        with path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
        return path

    def run_attempt(
        self,
        *,
        instance: dict,
        condition_id: str,
        attempt: int,
        env,
        agent,
        initial_workspace_hash: str | None,
    ) -> AttemptResult:
        instance_id = instance["instance_id"]
        trajectory_path = (
            self.trajectories_dir
            / instance_id
            / condition_id
            / f"{instance_id}__{condition_id}__a{attempt}.traj.json"
        )
        exit_status = None
        submission = None
        error = None

        try:
            info = agent.run(instance["problem_statement"]) or {}
            exit_status = info.get("exit_status")
            submission = info.get("submission")
        except Exception as exc:  # keep trajectory/log even for failed attempts
            exit_status = type(exc).__name__
            error = f"{type(exc).__name__}: {exc}"
            info = {"exception": error, "traceback": traceback.format_exc()}

        current_hash = self.workspace_hash(env)
        prediction_path = self.append_prediction(
            instance_id=instance_id,
            condition_id=condition_id,
            attempt=attempt,
            submission=submission,
        )
        self.save_agent(
            agent,
            trajectory_path,
            {
                "info": {
                    "exit_status": exit_status,
                    "submission": submission,
                    "pilot_condition": condition_id,
                    "pilot_attempt": attempt,
                    "initial_workspace_hash": initial_workspace_hash,
                    "workspace_hash": current_hash,
                    **(info if isinstance(info, dict) else {}),
                },
                "instance_id": instance_id,
            },
        )

        record = AttemptRecord(
            instance_id=instance_id,
            condition=condition_id,
            attempt=attempt,
            resolved=None,
            run_mode="python-api",
            first_step_error=None,
            workspace_hash=current_hash,
            initial_workspace_hash=initial_workspace_hash,
            trajectory_path=str(trajectory_path),
            error=error or f"resolved_requires_swebench_evaluation:{prediction_path}",
        )
        append_jsonl(self.run_log, record)
        return AttemptResult(record=record, exit_status=exit_status, submission=submission)

    def run_instance_condition(self, *, instance_id: str, condition_id: str, max_attempts: int) -> None:
        condition = get_condition(condition_id)
        instance = self.load_instance(instance_id)

        shared_env = None
        shared_agent = None
        initial_hash = None

        try:
            if condition.world_policy == WorldPolicy.RETAIN:
                shared_env = self.make_env(instance)
                initial_hash = self.workspace_hash(shared_env)
            if condition.context_policy == ContextPolicy.RETAIN and shared_env is not None:
                shared_agent = self.make_agent(shared_env)

            for attempt in range(1, max_attempts + 1):
                env = shared_env
                agent = shared_agent
                attempt_initial_hash = initial_hash

                if condition.world_policy == WorldPolicy.RESET:
                    env = self.make_env(instance)
                    attempt_initial_hash = self.workspace_hash(env)
                if condition.context_policy == ContextPolicy.RESET:
                    agent = self.make_agent(env)

                assert env is not None and agent is not None
                result = self.run_attempt(
                    instance=instance,
                    condition_id=condition_id,
                    attempt=attempt,
                    env=env,
                    agent=agent,
                    initial_workspace_hash=attempt_initial_hash,
                )
                print(
                    f"[python-api] {instance_id} {condition_id} a{attempt} "
                    f"exit_status={result.exit_status} resolved={result.record.resolved}"
                )

                if condition.world_policy == WorldPolicy.RESET and hasattr(env, "cleanup"):
                    env.cleanup()
        finally:
            if shared_env is not None and hasattr(shared_env, "cleanup"):
                shared_env.cleanup()

    def run(self, *, instance_ids: list[str], condition_ids: list[str], max_attempts: int) -> None:
        for instance_id in instance_ids:
            for condition_id in condition_ids:
                self.run_instance_condition(
                    instance_id=instance_id,
                    condition_id=condition_id,
                    max_attempts=max_attempts,
                )
