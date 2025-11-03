"""Instruction intention extraction stage."""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Sequence

    from impactscan.models import InstructionIntention


async def extract_intention(
    instruction: str,
    *,
    extra_keywords: Sequence[str] | None = None,
) -> InstructionIntention:
    """Derive the normalized instruction intention."""
    msg = "Intention extraction is not yet implemented."
    raise NotImplementedError(msg)


__all__ = ["extract_intention"]
