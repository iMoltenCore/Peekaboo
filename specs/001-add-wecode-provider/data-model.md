# Phase 1 Data Model: Add Wecode Provider

## Entity: Provider Configuration

- **Fields**
  - **providerId**: Identifier for provider selection (e.g., "wecode").
  - **displayName**: Human-readable provider name.
  - **enabled**: Whether provider is available for selection.
  - **models**: Supported model identifiers for Wecode.
- **Relationships**
  - Selected by CLI or runtime when choosing a provider.
- **Validation Rules**
  - providerId must be non-empty and unique among providers.

## Entity: Stream Chunk

- **Fields**
  - **index**: Order of the chunk in the stream.
  - **content**: Text content for the chunk.
  - **timestamp**: Emission time for ordering and diagnostics.
- **Relationships**
  - Aggregated into a Combined Response when non-streaming output is requested.
- **Validation Rules**
  - index must be monotonic within a stream.
  - content may be empty only for stream metadata events.

## Entity: Combined Response

- **Fields**
  - **text**: Full response created by concatenating chunks in order.
  - **chunkCount**: Number of chunks aggregated.
  - **completed**: Whether the stream reached a successful end state.
- **Relationships**
  - Derived from Stream Chunks produced by Wecode.
- **Validation Rules**
  - text must preserve original chunk order.
  - completed must be false if any chunk indicates an error.
