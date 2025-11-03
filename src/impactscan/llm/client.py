"""Protocol definitions for LLM clients."""
from __future__ import annotations

from typing import Any, Literal, Protocol, TypedDict


class Message(TypedDict):
    """Represents a single chat message for an LLM conversation."""

    role: Literal["system", "user", "assistant"]
    content: str


class LLMResponse(TypedDict, total=False):
    """Standardized response container for LLM invocations."""

    text: str | None
    json: dict[str, Any] | None
    usage: dict[str, int]
    raw: Any


class LLMClient(Protocol):
    """Vendor-agnostic interface that all LLM clients must satisfy."""

    async def chat(
        self,
        messages: list[Message],
        *,
        response_format: dict[str, Any] | None = None,
        tools: list[dict[str, Any]] | None = None,
        temperature: float = 0.2,
        max_tokens: int | None = None,
        model_hint: str | None = None,
    ) -> LLMResponse:
        """Send a chat completion request and return the normalized response."""
        ...


__all__ = ["LLMClient", "LLMResponse", "Message"]
