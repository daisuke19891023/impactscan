"""Custom exception hierarchy for ImpactScan."""
from __future__ import annotations


class ImpactScanError(Exception):
    """Base class for ImpactScan specific exceptions."""


class RipgrepNotFoundError(ImpactScanError):
    """Raised when the ripgrep executable cannot be located."""


class LLMResponseFormatError(ImpactScanError):
    """Raised when an LLM response fails schema validation after retries."""


class RateLimitExceededError(ImpactScanError):
    """Raised when configured rate limits are exceeded."""


class ConfigError(ImpactScanError):
    """Raised when user configuration is invalid or incomplete."""


__all__ = [
    "ConfigError",
    "ImpactScanError",
    "LLMResponseFormatError",
    "RateLimitExceededError",
    "RipgrepNotFoundError",
]
