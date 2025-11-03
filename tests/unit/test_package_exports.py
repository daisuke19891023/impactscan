"""Smoke tests for top-level package exports."""

import importlib


def test_public_exports_available() -> None:
    """Ensure the primary entrypoints are importable from the package root."""
    module = importlib.import_module("impactscan")
    assert hasattr(module, "ImpactScanEngine")
    assert hasattr(module, "ImpactScanConfig")
    assert hasattr(module, "ImpactScanError")
    assert hasattr(module, "ImpactAssessment")
    assert hasattr(module, "ImpactRunSummary")
