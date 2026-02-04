# Contracts: Wecode Text Generation

## Endpoint: Stream Text

- **Action**: Stream text output from Wecode.
- **Request**:
  - **input**: User prompt text.
  - **model**: Selected Wecode model identifier.
  - **options**: Optional generation controls (temperature, max tokens).
- **Stream Response**:
  - **chunkIndex**: Incrementing index.
  - **content**: Text content for the chunk.
  - **done**: True when streaming completes successfully.
  - **error**: Error detail when streaming fails.

## Endpoint: General Text (Aggregated)

- **Action**: Provide a single combined text response for non-streaming requests.
- **Request**:
  - **input**: User prompt text.
  - **model**: Selected Wecode model identifier.
  - **options**: Optional generation controls (temperature, max tokens).
- **Response**:
  - **text**: Combined output constructed from streamed content.
  - **chunkCount**: Number of chunks aggregated.
  - **error**: Error detail when streaming fails before completion.
