"""Cache store abstractions used by ImpactScan."""
from __future__ import annotations



class CacheStore:
    """Abstract cache interface for ImpactScan components."""

    def get(self, namespace: str, key: str) -> bytes | None:
        """Retrieve a cached value."""
        msg = "CacheStore.get is not yet implemented."
        raise NotImplementedError(msg)

    def set(
        self,
        namespace: str,
        key: str,
        value: bytes,
        ttl_sec: int | None = None,
    ) -> None:
        """Store a cached value."""
        msg = "CacheStore.set is not yet implemented."
        raise NotImplementedError(msg)


class SQLiteCacheStore(CacheStore):
    """SQLite-backed cache implementation."""


__all__ = ["CacheStore", "SQLiteCacheStore"]
