"""Built-in adapters that implement :class:`impactscan.llm.client.LLMClient`."""
from __future__ import annotations

from collections.abc import Awaitable, Mapping
import typing as t
from typing import Any

from impactscan.llm.client import LLMClient, LLMResponse, Message


class AzureOpenAIAdapter(LLMClient):
    """Adapter for Azure OpenAI deployments."""

    def __init__(
        self,
        *,
        endpoint: str,
        api_key: str,
        deployment: str,
        api_version: str | None = None,
        rpm_limit: int | None = None,
        tpm_limit: int | None = None,
    ) -> None:
        """Store Azure-specific connection information."""
        self.endpoint = endpoint
        self.api_key = api_key
        self.deployment = deployment
        self.api_version = api_version
        self.rpm_limit = rpm_limit
        self.tpm_limit = tpm_limit

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
        """Send a chat completion request."""
        msg = "Azure OpenAI adapter has not been implemented yet."
        raise NotImplementedError(msg)


class OpenAIAdapter(LLMClient):
    """Adapter for the public OpenAI API."""

    def __init__(
        self,
        *,
        api_key: str,
        model: str,
        rpm_limit: int | None = None,
        tpm_limit: int | None = None,
    ) -> None:
        """Store OpenAI connection information."""
        self.api_key = api_key
        self.model = model
        self.rpm_limit = rpm_limit
        self.tpm_limit = tpm_limit

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
        """Send a chat completion request."""
        msg = "OpenAI adapter has not been implemented yet."
        raise NotImplementedError(msg)


class CallableAdapter(LLMClient):
    """Wraps an arbitrary callable that mimics the LLM response signature."""

    def __init__(self, func: t.Callable[..., Any]) -> None:
        """Store the wrapped callable."""
        self._func = func

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
        """Delegate to the wrapped callable and normalize the response."""
        call_result = t.cast(
            "Mapping[str, Any] | Awaitable[Mapping[str, Any]]",
            self._func(
                messages,
                response_format=response_format,
                tools=tools,
                temperature=temperature,
                max_tokens=max_tokens,
                model_hint=model_hint,
            ),
        )
        if isinstance(call_result, Awaitable):
            candidate = await call_result
        else:
            candidate = call_result
        return t.cast("LLMResponse", dict(candidate))


__all__ = ["AzureOpenAIAdapter", "CallableAdapter", "OpenAIAdapter"]
