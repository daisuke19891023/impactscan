# ImpactScan Design Template

## 1. Architectural Goals
- Async-first pipeline with synchronous wrappers for compatibility.
- Dependency injection for key subsystems (LLM clients, cache, scanner, classifier, report writers).
- Self-initialization path using environment-provided API keys when DI is not supplied.

## 2. High-level Flow
1. **Intention Extraction:** Small-model LLM normalizes user instruction and perspectives.
2. **Scanning:** Ripgrep identifies candidate matches across configured globs.
3. **Preprocessing:** Non-code ranges filtered via Tree-sitter → Pygments → heuristics fallback.
4. **Triage:** Small-model LLM classifies candidate windows (`drop|keep|maybe`).
5. **Analysis:** Large-model LLM produces JSON-schema-compliant impact assessments.
6. **Reporting:** CSV/JSONL writers persist assessments; optional Markdown summary aggregates run metrics.

## 3. Module Responsibilities
- `impactscan.engine`: Orchestrates pipeline stages, enforces configuration, exposes sync/async APIs.
- `impactscan.config`: Pydantic models capturing runtime configuration and provider settings.
- `impactscan.models`: Pydantic domain models for instructions, candidates, triage, assessments, and summaries.
- `impactscan.scanner.ripgrep`: Abstraction over ripgrep CLI with async streaming support.
- `impactscan.preprocess.classifier`: Interfaces for Tree-sitter/Pygments/heuristic classifiers.
- `impactscan.llm.client`: Protocol for pluggable LLM clients; `llm.adapters` hosts built-in adapters.
- `impactscan.pipeline.*`: Stage-specific coordination logic (intention, triage, analysis).
- `impactscan.report.writer`: Output utilities for CSV/JSONL/Markdown.
- `impactscan.cache.store`: Cache abstraction with SQLite reference implementation.
- `impactscan.concurrency.limiter`: Rate limiter and retry helpers.

## 4. Data Contracts
- **InstructionIntention:** Normalized instruction plus keyword and perspective metadata.
- **CandidateFileWindow:** Aggregated ripgrep hits with spans and classification metadata.
- **TriageResult:** Decision, score, and hints for each candidate window.
- **ImpactAssessment:** JSON schema aligned record for downstream reporting.
- **ImpactRunSummary:** Aggregate metrics and file paths produced by a run.

## 5. LLM Integration Strategy
- `LLMClient` protocol abstracts vendor-specific behavior.
- Built-in adapters manage HTTP transport, authentication, and rate limits (to be implemented).
- Response normalization ensures consistent token usage accounting and structured output validation.
- Retry/backoff policies handled via concurrency utilities and Tenacity-based helpers.

## 6. Extensibility Points
- Custom scanner, classifier, cache, or LLM client can be supplied by implementing documented interfaces.
- Additional report formats can be registered alongside CSV/JSONL writers.
- Future CLI package may wrap `ImpactScanEngine` for command-line automation.

## 7. Outstanding Tasks
- Implement concrete logic for each pipeline stage and adapter.
- Define Tree-sitter grammar packaging strategy and fallback heuristics.
- Establish caching schema and SQLite persistence model.
- Author integration and unit tests covering pipeline orchestration and failure handling.
- Document CLI usage patterns and configuration examples in `docs/reference/`.
