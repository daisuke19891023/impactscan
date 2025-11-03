"""Configuration models for ImpactScan."""
from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field, ValidationError

from impactscan.errors import ConfigError


def _default_deployments() -> dict[Literal["small", "large"], str]:
    """Return an empty mapping for deployment names."""
    return {}


class RipgrepConfig(BaseModel):
    """Configuration for ripgrep search behavior."""

    context_lines: int = Field(default=12, ge=0)
    fixed_strings: bool = True
    smart_case: bool = True
    threads: int = Field(default=0, ge=0)
    include_hidden: bool = False


class PreprocessConfig(BaseModel):
    """Configuration for preprocessing and non-code filtering."""

    drop_comment_lines: bool = True
    analyzer: Literal["tree-sitter", "pygments", "heuristics"] = "tree-sitter"
    keep_string_literals: bool = True
    string_weight_penalty: float = Field(default=0.15, ge=0.0, le=1.0)
    detect_if0_blocks: bool = True
    cache_noncode_ranges: bool = True
    max_file_bytes_for_parse: int = Field(default=2_000_000, gt=0)
    merge_window_lines: int = Field(default=40, ge=1)
    max_tokens_file_context: int = Field(default=2000, ge=1)


class AzureOpenAIConfig(BaseModel):
    """Configuration for Azure OpenAI deployments."""

    enabled: bool = False
    endpoint: str | None = None
    api_key_env: str | None = "AZURE_OPENAI_API_KEY"
    api_version: str | None = "2024-xx-xx"
    deployments: dict[Literal["small", "large"], str] = Field(default_factory=_default_deployments)


class OpenAIConfig(BaseModel):
    """Configuration for OpenAI API usage."""

    enabled: bool = False
    api_key_env: str | None = "OPENAI_API_KEY"
    model_small: str | None = None
    model_large: str | None = None


class OutputConfig(BaseModel):
    """Configuration for report writing outputs."""

    dir: str = "./reports"
    write_csv: bool = True
    write_jsonl: bool = True
    write_summary_md: bool = False


class AnalysisConfig(BaseModel):
    """Configuration values for triage and analysis routines."""

    perspectives: list[str] = Field(
        default_factory=lambda: ["セキュリティ", "後方互換性", "パフォーマンス", "テスト影響"],
    )
    triage_threshold: float = Field(default=0.35, ge=0.0, le=1.0)
    parallelism: int = Field(default=16, ge=1)
    rpm_limit: int | None = Field(default=900, ge=1)
    tpm_limit: int | None = Field(default=1_000_000, ge=1)


class ImpactScanConfig(BaseModel):
    """Top-level configuration for the ImpactScan engine."""

    target_dir: str
    include_globs: list[str] = Field(default_factory=lambda: ["**/*"])
    exclude_globs: list[str] = Field(
        default_factory=lambda: [
            "**/.git/**",
            "**/node_modules/**",
            "**/dist/**",
            "**/*.min.js",
        ],
    )
    ripgrep: RipgrepConfig = Field(default_factory=RipgrepConfig)
    preprocess: PreprocessConfig = Field(default_factory=PreprocessConfig)
    analysis: AnalysisConfig = Field(default_factory=AnalysisConfig)
    azure_openai: AzureOpenAIConfig = Field(default_factory=AzureOpenAIConfig)
    openai: OpenAIConfig = Field(default_factory=OpenAIConfig)
    output: OutputConfig = Field(default_factory=OutputConfig)

    def __init__(self, **data: object) -> None:
        """Validate incoming data and surface ConfigError on failure."""
        try:
            super().__init__(**data)
        except ValidationError as exc:
            msg = "Invalid ImpactScan configuration"
            raise ConfigError(msg) from exc

        if not self.target_dir or not self.target_dir.strip():
            msg = "target_dir must be a non-empty string"
            raise ConfigError(msg)


__all__ = [
    "AnalysisConfig",
    "AzureOpenAIConfig",
    "ImpactScanConfig",
    "OpenAIConfig",
    "OutputConfig",
    "PreprocessConfig",
    "RipgrepConfig",
]
