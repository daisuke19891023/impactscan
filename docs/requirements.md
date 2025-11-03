# ImpactScan Requirements (v1.0 Proposal)

## 1. Overview
- **Purpose:** Automate impact analysis from natural-language change instructions through reporting.
- **Key Capabilities:** ripgrep scanning, non-code filtering, LLM triage and analysis, CSV/JSONL outputs.
- **Consumption:** Reusable Python package with async-first APIs and optional CLI extensions.

## 2. Functional Requirements
1. Accept change instructions and optional keyword hints.
2. Extract normalized intent and keywords via LLM (small model).
3. Run ripgrep searches with configuration-driven scope control.
4. Filter non-code matches using Tree-sitter first, falling back to Pygments or heuristics.
5. Perform staged LLM processing: triage with a small model, detailed analysis with a large model.
6. Persist structured assessments to CSV and JSONL, with optional Markdown summary.
7. Support dependency injection for LLM clients as well as self-initialization via API keys.
8. Provide caching for LLM results and preprocessing artifacts.
9. Expose synchronous wrappers for critical async APIs.

## 3. Non-functional Requirements
- **Performance:** Stream ripgrep results, parallelize LLM calls, respect RPM/TPM limits.
- **Reliability:** Retry transient LLM failures with exponential backoff; cache repeated work.
- **Extensibility:** Allow custom implementations for scanning, classification, LLM access, caching, and reporting.
- **Portability:** Support Windows, macOS, and Linux assuming ripgrep availability.
- **Security:** Load credentials from environment, support future extensions for masking sensitive data.

## 4. External Dependencies
- ripgrep CLI available on PATH.
- Tree-sitter grammars (preferred) with Pygments fallback.
- Network access to configured LLM providers when using default adapters.

## 5. Configuration Summary
- `ImpactScanConfig` controls directories, globs, analysis parameters, LLM provider settings, and outputs.
- Supports Azure OpenAI and OpenAI providers with environment-variable-based API key lookup.
- Output directory defaults to `./reports` with CSV and JSONL enabled.

## 6. Deliverables
- Python package under `src/impactscan/` exposing configuration models, engine facade, and key services.
- Documentation set including this requirements outline and companion design notes.
- Automated quality gates via Ruff (lint/format) and Pyright typing checks.

## 7. Open Questions / Future Work
- CLI packaging specifics and UX design.
- Concrete caching backends beyond SQLite prototype.
- Strategy for masking sensitive data in prompts and outputs.
- Additional report formats (HTML, BigQuery, Parquet) and integration hooks.
