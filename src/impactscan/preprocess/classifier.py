"""Non-code range classification interfaces."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class NonCodeRanges:
    """Represents the ranges of non-code artifacts in a source file."""

    comment_spans: list[tuple[int, int]]
    string_spans: list[tuple[int, int]]
    disabled_spans: list[tuple[int, int]]


class NonCodeClassifier:
    """Interface for building non-code ranges."""

    async def build_ranges(self, path: str, content: bytes, lang: str | None) -> NonCodeRanges:
        """Compute non-code ranges asynchronously."""
        raise NotImplementedError

    def build_ranges_sync(self, path: str, content: bytes, lang: str | None) -> NonCodeRanges:
        """Compute non-code ranges synchronously."""
        raise NotImplementedError


class TreeSitterClassifier(NonCodeClassifier):
    """Tree-sitter backed implementation."""


class PygmentsClassifier(NonCodeClassifier):
    """Pygments backed implementation."""


class HeuristicClassifier(NonCodeClassifier):
    """Lightweight heuristic implementation."""


def classify_hit(
    byte_offset: int,
    ranges: NonCodeRanges,
    keep_strings: bool,
) -> str:
    """Classify a ripgrep hit based on non-code ranges."""
    raise NotImplementedError


__all__ = [
    "HeuristicClassifier",
    "NonCodeClassifier",
    "NonCodeRanges",
    "PygmentsClassifier",
    "TreeSitterClassifier",
    "classify_hit",
]
