# ImpactScan Implementation Tasks (v1.0 proposal)

## Definition of Done (applies to every task group)
- ✅ `impactscan` package is installable via `uv pip install -e .` and imports without side effects.
- ✅ Public entrypoints `ImpactScanEngine` and `ImpactScanConfig` are importable from `impactscan`.
- ✅ Pyright strict type checking (`uv run nox -s typing`) and Ruff linting (`uv run nox -s lint`) pass.
- ✅ Pytest suite (unit + async) succeeds with coverage ≥ 85% once later pipeline stages land.
- ✅ Sample execution with mock LLM writes CSV and JSONL artifacts in the documented schema.

> **Note:** Original draft referenced `mypy`; ImpactScan standardizes on **Pyright** for static analysis.

---

## Task Group T1 – Package initialization & build infrastructure

### T1-01 Package skeleton & editable install
**Work items**
- Define project metadata and dependencies in `pyproject.toml` (runtime: `pydantic`, `httpx`, `tenacity`, `orjson`, `tree_sitter`, `pygments`; dev: `pytest`, `pytest-asyncio`, `ruff`, `pyright`, etc.).
- Ensure source layout `src/impactscan/` with `__init__.py` aggregating public symbols: `ImpactScanEngine`, `ImpactScanConfig`, `ImpactScanError`, `ImpactAssessment`, `ImpactRunSummary`.
- Provide `uv` workflow documentation (nox sessions) to support `uv pip install -e .` / `uv sync` flows.

**Acceptance criteria**
- ✅ `uv pip install -e .` installs the package without errors.
- ✅ `python -c "from impactscan import ImpactScanConfig, ImpactScanEngine; print('ok')"` succeeds.

**Unit tests**
- Import smoke test asserting public exports resolve (skip if dependencies unavailable).

### T1-02 CI / quality gates (recommended)
**Work items**
- Configure GitHub Actions workflow invoking `uv run nox -s lint`, `uv run nox -s typing`, and `uv run nox -s test -p linux` on pushes and PRs targeting `main`.
- Cache the uv / nox virtualenv for performance.

**Acceptance criteria**
- ✅ Workflow runs automatically on `main` and pull requests, finishing green with baseline skeleton.

**Unit tests**
- Not required; workflow definition is reviewed manually.

---

## Task Group T2 – Configuration & data models

### T2-01 `ImpactScanConfig` (Pydantic)
**Work items**
- Implement configuration models in `impactscan/config.py` with nested sections for ripgrep, preprocessing, analysis, provider adapters, and output.
- Validate `target_dir` presence (non-empty), propagate `include_globs` / `exclude_globs`, and allow operation when all provider toggles are disabled (DI injects mock LLMs).
- Guard against invalid numeric settings (e.g., negative `parallelism`) and re-raise issues as `ConfigError`.
- (Optional) Provide YAML loader helper that feeds into the Pydantic models.

**Acceptance criteria**
- ✅ Missing `target_dir` raises `ConfigError` with helpful context.
- ✅ `include_globs` / `exclude_globs` lists are respected and default to sensible values.
- ✅ Both `azure_openai.enabled` and `openai.enabled` may be `False`; engine relies on dependency injection instead.

**Unit tests**
- Validate defaults, numeric bounds, DI-friendly toggles, and error handling (negative parallelism, blank target directory).

### T2-02 Domain data models (`models.py`)
**Work items**
- Define strongly-typed Pydantic models for intention, ripgrep hits, triage, assessments, and run summaries.
- Enforce validation rules: `ImpactAssessment.perspective_scores` in `[0,1]`, `CandidateFileWindow.spans` as `(start_line, end_line)` tuples, mandatory fields for `ImpactAssessment`.
- Provide defaults for optional collections and ensure serialization stability.

**Acceptance criteria**
- ✅ Missing mandatory assessment fields surface as Pydantic validation errors.
- ✅ Perspective scores outside `[0, 1]` are rejected.
- ✅ `CandidateFileWindow.spans` stored as ordered tuples `(start_line, end_line)`.

**Unit tests**
- Cover normal and failure cases: required-field enforcement, span validation, and score bounds.

---

## Status Tracking
| Task | Status | Notes |
|------|--------|-------|
| T1-01 | ✅ Done | Package skeleton, exports, editable install smoke tested. |
| T1-02 | ⏳ Pending | Workflow scaffolding to be added once CI environment defined. |
| T2-01 | ✅ Done | Config models validate inputs, raise `ConfigError`, defaults documented. |
| T2-02 | ✅ Done | Domain models enforce span and score rules via Pydantic validators. |

