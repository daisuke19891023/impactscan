"""Concurrency utilities such as rate limiters."""
from __future__ import annotations


class RateLimiter:
    """Placeholder rate limiter implementation."""

    def __init__(self, *, rpm_limit: int | None = None, tpm_limit: int | None = None) -> None:
        """Store rate limit configuration."""
        self.rpm_limit = rpm_limit
        self.tpm_limit = tpm_limit

    async def acquire(self, tokens: int = 0) -> None:
        """Acquire capacity for a request."""
        msg = "RateLimiter.acquire is not yet implemented."
        raise NotImplementedError(msg)


__all__ = ["RateLimiter"]
