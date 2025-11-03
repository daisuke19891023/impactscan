"""High level ImpactScan engine facade."""
from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING

from impactscan.errors import ConfigError

if TYPE_CHECKING:
    from collections.abc import AsyncIterator, Iterable, Sequence

    from impactscan.config import ImpactScanConfig
    from impactscan.llm.client import LLMClient
    from impactscan.models import ImpactAssessment, ImpactRunSummary


class ImpactScanEngine:
    """Coordinates the end-to-end ImpactScan workflow."""

    def __init__(
        self,
        config: ImpactScanConfig,
        llm_small: LLMClient | None = None,
        llm_large: LLMClient | None = None,
    ) -> None:
        """Store configuration and optional LLM clients."""
        self.config = config
        self._llm_small = llm_small
        self._llm_large = llm_large

    async def run(
        self,
        *,
        instruction: str,
        extra_keywords: Sequence[str] | None = None,
    ) -> ImpactRunSummary:
        """Run the full pipeline and return a summary."""
        msg = "Pipeline execution is not yet implemented."
        raise NotImplementedError(msg)

    async def iter_assessments(
        self,
        *,
        instruction: str,
        extra_keywords: Sequence[str] | None = None,
    ) -> AsyncIterator[ImpactAssessment]:
        """Yield detailed assessments as soon as they are ready."""
        msg = "Assessment streaming is not yet implemented."
        raise NotImplementedError(msg)

    def run_sync(
        self,
        *,
        instruction: str,
        extra_keywords: Sequence[str] | None = None,
    ) -> ImpactRunSummary:
        """Run the asynchronous pipeline synchronously."""
        return asyncio.run(self.run(instruction=instruction, extra_keywords=extra_keywords))

    def iter_assessments_sync(
        self,
        *,
        instruction: str,
        extra_keywords: Sequence[str] | None = None,
    ) -> Iterable[ImpactAssessment]:
        """Stream assessments synchronously."""
        msg = "Synchronous assessment streaming is not yet implemented."
        raise NotImplementedError(msg)

    def require_small_client(self) -> LLMClient:
        """Return the configured small LLM client or raise an error."""
        if self._llm_small is None:
            msg = "Small LLM client is not configured."
            raise ConfigError(msg)
        return self._llm_small

    def require_large_client(self) -> LLMClient:
        """Return the configured large LLM client or raise an error."""
        if self._llm_large is None:
            msg = "Large LLM client is not configured."
            raise ConfigError(msg)
        return self._llm_large


__all__ = ["ImpactScanEngine"]
