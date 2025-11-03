"""Ripgrep scanner interface and implementation."""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import AsyncIterator, Iterable, Sequence

    from impactscan.config import ImpactScanConfig
    from impactscan.models import CandidateHit


class RipgrepScanner:
    """Wrapper around the ripgrep command line interface."""

    def __init__(self, config: ImpactScanConfig) -> None:
        """Initialize the scanner with runtime configuration."""
        self.config = config

    async def search(self, *, must_keywords: Sequence[str]) -> AsyncIterator[CandidateHit]:
        """Stream ripgrep matches asynchronously."""
        msg = "Ripgrep async search is not yet implemented."
        raise NotImplementedError(msg)

    def search_sync(self, *, must_keywords: Sequence[str]) -> Iterable[CandidateHit]:
        """Return ripgrep matches synchronously."""
        msg = "Ripgrep sync search is not yet implemented."
        raise NotImplementedError(msg)


__all__ = ["RipgrepScanner"]
