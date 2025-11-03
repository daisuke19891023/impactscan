"""Tests for ImpactScan domain Pydantic models."""

import pytest

from impactscan.models import CandidateFileWindow, ImpactAssessment
from pydantic import ValidationError


def test_candidate_file_window_span_validation() -> None:
    """Spans must be two-length tuples with ordered, positive integers."""
    window = CandidateFileWindow.model_validate({"file": "sample.py", "spans": [(1, 3), [5, 8]]})
    assert window.spans == [(1, 3), (5, 8)]


def test_candidate_file_window_invalid_span_shape() -> None:
    """Invalid span entries should trigger validation errors."""
    with pytest.raises(ValidationError):
        CandidateFileWindow.model_validate({"file": "sample.py", "spans": [(0, 1)]})


def test_impact_assessment_requires_fields() -> None:
    """Missing mandatory fields should raise a validation error."""
    with pytest.raises(ValidationError):
        ImpactAssessment.model_validate({"file": "sample.py", "reason": "missing", "confidence": 0.5})


def test_impact_assessment_perspective_scores_bounds() -> None:
    """Perspective scores outside [0, 1] are rejected."""
    with pytest.raises(ValidationError):
        ImpactAssessment.model_validate(
            {
                "file": "sample.py",
                "impact_level": "high",
                "reason": "bad score",
                "confidence": 0.8,
                "perspective_scores": {"security": 1.5},
            },
        )


def test_impact_assessment_accepts_valid_scores() -> None:
    """Valid perspective scores pass validation."""
    assessment = ImpactAssessment(
        file="sample.py",
        impact_level="low",
        reason="ok",
        confidence=0.3,
        perspective_scores={"security": 0.2, "performance": 1.0},
        lines=["line"],
        num_occurrences=2,
    )
    assert assessment.perspective_scores["performance"] == 1.0
    assert assessment.num_occurrences == 2
