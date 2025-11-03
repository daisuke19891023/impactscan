"""Detailed analysis stage implementation."""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable

    from impactscan.models import ImpactAssessment, InstructionIntention, TriageResult


async def run_analysis(
    triage_results: Iterable[TriageResult],
    *,
    intention: InstructionIntention,
) -> list[ImpactAssessment]:
    """Execute the heavy-weight LLM analysis stage."""
    msg = "Analysis execution is not yet implemented."
    raise NotImplementedError(msg)


__all__ = ["run_analysis"]
