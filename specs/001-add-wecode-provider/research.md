# Research: Add Wecode Provider

## Decision 1: Aggregate stream for non-streaming requests

**Decision**: Implement `generateText` by collecting `streamText` deltas into a
single response.

**Rationale**: `GoogleProvider` already aggregates `streamText` into a
`ProviderResponse`, collecting text, tool calls, usage, and finish reason. This
matches the requirement that Wecode does not support non-streaming directly.

**Alternatives considered**:

- Implement a separate non-streaming API path. Rejected because Wecode does not
  support it and it would duplicate logic.

## Decision 2: Use existing stream delta conventions

**Decision**: Follow `TextStreamDelta` conventions for text, tool calls, and done
events, and derive usage/finish reason from the done event.

**Rationale**: `TextStreamDelta` is the canonical stream type in Tachikoma, and
providers already emit `.text`, `.tool`, and `.done`. `GoogleProvider` uses this
pattern and overrides finish reason to `.toolCalls` when tool calls are present.

**Alternatives considered**:

- Custom stream event types. Rejected because it would break provider parity and
  require downstream changes.

## Decision 3: Keep changes minimal and provider-local

**Decision**: Implement Wecode logic within `WecodeProvider` and reuse shared
helpers only if they already exist.

**Rationale**: The constitution requires minimal changes and generic abstractions
only when they reduce duplication. `GoogleProvider` shows a small, local
aggregation pattern that can be reused without new shared utilities.

**Alternatives considered**:

- Add a new shared aggregator helper. Deferred unless multiple providers need it.
