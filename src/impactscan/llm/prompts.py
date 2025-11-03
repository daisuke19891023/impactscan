"""Internal prompt templates used by the ImpactScan pipeline."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PromptTemplate:
    """Simple container for prompt template metadata."""

    name: str
    system: str
    user: str


DEFAULT_INTENTION_PROMPT = PromptTemplate(
    name="intention",
    system="You are an assistant that extracts structured intents for repository impact analysis.",
    user="""Instruction: {instruction}\nExtra keywords: {extra_keywords}\nReturn JSON with intention and keywords.""",
)


__all__ = ["DEFAULT_INTENTION_PROMPT", "PromptTemplate"]
