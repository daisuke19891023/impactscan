"""Tests for ImpactScan configuration models."""

import pytest

from impactscan.config import ImpactScanConfig
from impactscan.errors import ConfigError


def test_config_requires_target_dir() -> None:
    """Missing target_dir should raise ConfigError instead of ValidationError."""
    with pytest.raises(ConfigError):
        ImpactScanConfig()


def test_config_rejects_blank_target_dir() -> None:
    """Whitespace-only target directories are invalid."""
    with pytest.raises(ConfigError):
        ImpactScanConfig(target_dir="   ")


def test_config_defaults_include_and_exclude_globs() -> None:
    """Defaults should contain broad include and opinionated exclude patterns."""
    config = ImpactScanConfig(target_dir="./repo")
    assert config.include_globs == ["**/*"]
    assert "**/.git/**" in config.exclude_globs


def test_config_allows_disabled_providers() -> None:
    """Configuration should not force Azure/OpenAI providers when DI is used."""
    config = ImpactScanConfig(target_dir=".")
    assert not config.azure_openai.enabled
    assert not config.openai.enabled


def test_config_parallelism_must_be_positive() -> None:
    """Invalid analysis parallelism should surface as a ConfigError."""
    with pytest.raises(ConfigError):
        ImpactScanConfig(target_dir=".", analysis={"parallelism": 0})
