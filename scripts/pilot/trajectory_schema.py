"""JSONL schema helpers for pilot trajectory logs."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


@dataclass
class AttemptRecord:
    instance_id: str
    condition: str
    attempt: int
    resolved: bool | None
    run_mode: str = "unknown"
    first_step_error: bool | None = None
    pre_attempt_workspace_hash: str | None = None
    workspace_hash: str | None = None
    initial_workspace_hash: str | None = None
    context_token_count: int | None = None
    trajectory_path: str | None = None
    mini_swe_output: str | None = None
    error: str | None = None
    timestamp: str = field(default_factory=utc_now_iso)

    def to_json(self) -> str:
        return json.dumps(asdict(self), ensure_ascii=False)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> AttemptRecord:
        return cls(**{k: v for k, v in data.items() if k in cls.__dataclass_fields__})


def append_jsonl(path: Path, record: AttemptRecord) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(record.to_json() + "\n")


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows
