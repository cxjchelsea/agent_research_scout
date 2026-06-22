"""Retry condition definitions for dual-state contamination pilot."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Literal


class ContextPolicy(str, Enum):
    RETAIN = "retain"
    RESET = "reset"


class WorldPolicy(str, Enum):
    RETAIN = "retain"
    RESET = "reset"


ConditionId = Literal["dirty-retry", "clean-restart", "full-reset"]


@dataclass(frozen=True)
class Condition:
    id: ConditionId
    context_policy: ContextPolicy
    world_policy: WorldPolicy
    description: str

    def attempt_label(self, attempt: int) -> str:
        return f"{self.id}@attempt{attempt}"


CONDITIONS: dict[ConditionId, Condition] = {
    "dirty-retry": Condition(
        id="dirty-retry",
        context_policy=ContextPolicy.RETAIN,
        world_policy=WorldPolicy.RETAIN,
        description="Keep failed attempt in ContextState and WorldState",
    ),
    "clean-restart": Condition(
        id="clean-restart",
        context_policy=ContextPolicy.RESET,
        world_policy=WorldPolicy.RETAIN,
        description="Reset ContextState on retry; retain WorldState edits",
    ),
    "full-reset": Condition(
        id="full-reset",
        context_policy=ContextPolicy.RESET,
        world_policy=WorldPolicy.RESET,
        description="Reset ContextState and restore WorldState snapshot on retry",
    ),
}


def get_condition(condition_id: str) -> Condition:
    if condition_id not in CONDITIONS:
        raise ValueError(f"Unknown condition: {condition_id}. Expected one of {list(CONDITIONS)}")
    return CONDITIONS[condition_id]  # type: ignore[index]
