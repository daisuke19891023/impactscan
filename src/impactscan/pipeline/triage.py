"""LLM powered triage stage."""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable

    from impactscan.models import CandidateFileWindow, InstructionIntention, TriageResult


async def run_triage(
    windows: Iterable[CandidateFileWindow],
    *,
    intention: InstructionIntention,
) -> list[TriageResult]:
    """Execute the triage stage for provided windows."""
    msg = "Triage execution is not yet implemented."
    raise NotImplementedError(msg)


__all__ = ["run_triage"]
