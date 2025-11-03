"""Report writers for ImpactScan outputs."""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable, Mapping
    from typing import Any

    from impactscan.models import ImpactAssessment


def write_csv(path: str, items: Iterable[ImpactAssessment]) -> None:
    """Write assessments to a CSV file."""
    msg = "CSV writer is not yet implemented."
    raise NotImplementedError(msg)


def write_jsonl(path: str, items: Iterable[ImpactAssessment]) -> None:
    """Write assessments to a JSON Lines file."""
    msg = "JSONL writer is not yet implemented."
    raise NotImplementedError(msg)


def write_summary_md(path: str, summary: Mapping[str, Any]) -> None:
    """Write a Markdown summary of the run."""
    msg = "Markdown summary writer is not yet implemented."
    raise NotImplementedError(msg)


__all__ = ["write_csv", "write_jsonl", "write_summary_md"]
