# Phase 0 Research: Add Wecode Provider

## Decision 1: Provider integration point

- **Decision**: Implement Wecode as a first-class provider in Tachikoma alongside
  existing providers, mirroring the Responses-style streaming interface.
- **Rationale**: Keeps provider logic centralized and matches current provider
  selection and model routing patterns.
- **Alternatives considered**: Treat Wecode as a custom provider only.

## Decision 2: Non-streaming text behavior

- **Decision**: Implement non-streaming text by collecting streamed chunks and
  returning a single combined response in order.
- **Rationale**: Wecode does not support non-streaming output directly, and
  aggregation preserves compatibility with existing text workflows.
- **Alternatives considered**: Disallow non-streaming requests for Wecode.

## Decision 3: CLI agent compatibility validation

- **Decision**: Validate with `peekaboo agent "hello"` using Wecode after
  integration and ensure missing credentials are surfaced with clear errors.
- **Rationale**: The agent path is the primary CLI entry for text generation and
  must work end-to-end.
- **Alternatives considered**: Only test via provider-specific unit tests.

## Decision 4: Local testing credential handling

- **Decision**: Use `/tmp/key` as the local API key source during manual testing.
- **Rationale**: Matches provided testing guidance and avoids committing secrets.
- **Alternatives considered**: Require real credentials or skip manual testing.
