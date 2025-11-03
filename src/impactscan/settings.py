"""Application settings for ImpactScan."""
from __future__ import annotations

from pydantic_settings import BaseSettings, SettingsConfigDict


class ImpactScanSettings(BaseSettings):
    """Environment-driven settings container."""

    azure_openai_api_key: str | None = None
    openai_api_key: str | None = None

    model_config = SettingsConfigDict(env_file=".env", env_prefix="IMPACTSCAN_")


__all__ = ["ImpactScanSettings"]
