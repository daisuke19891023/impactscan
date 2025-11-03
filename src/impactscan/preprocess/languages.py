"""Language detection helpers for ImpactScan."""
from __future__ import annotations


EXTENSION_TO_LANGUAGE: dict[str, str] = {
    ".py": "python",
    ".ts": "typescript",
    ".tsx": "tsx",
    ".js": "javascript",
    ".rs": "rust",
    ".go": "go",
}


__all__ = ["EXTENSION_TO_LANGUAGE"]
