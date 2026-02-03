---

description: "Task list for adding Wecode provider"
---

# Tasks: Add Wecode Provider

**Input**: Design documents from `/specs/001-add-wecode-provider/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/

**Tests**: Tests are REQUIRED (per constitution) and included below.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Prepare provider scaffolding and review baseline behavior

- [ ] T001 Review provider interfaces in `Tachikoma/Sources/Tachikoma/Core/Provider.swift` and `Tachikoma/Sources/Tachikoma/Providers/OpenAI/OpenAIResponsesProvider.swift`
- [ ] T002 Create Wecode provider folder and stub in `Tachikoma/Sources/Tachikoma/Providers/Wecode/WecodeProvider.swift`
- [ ] T003 [P] Add Wecode test scaffold in `Tachikoma/Tests/TachikomaTests/Providers/WecodeProviderTests.swift`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core wiring required before any user story work can proceed

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T004 Add Wecode model enum and metadata in `Tachikoma/Sources/Tachikoma/Models/Model.swift`
- [ ] T005 Update provider parsing for `wecode/<model>` in `Tachikoma/Sources/Tachikoma/Providers/ProviderParser.swift`
- [ ] T006 Wire Wecode provider creation in `Tachikoma/Sources/Tachikoma/Providers/ProviderFactory.swift`
- [ ] T007 Add Wecode display name and API key hint mapping in `Apps/CLI/Sources/PeekabooCLI/Commands/AI/AgentCommand.swift`
- [ ] T008 Ensure provider list parsing accepts Wecode in `Core/PeekabooCore/Sources/PeekabooAutomation/Utils/AIProviderParser.swift`

**Checkpoint**: Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - Stream text with Wecode (Priority: P1) 🎯 MVP

**Goal**: Stream text output using Wecode for CLI agent requests

**Independent Test**: Configure Wecode, run `peekaboo agent "hello"`, and observe streamed output.

### Tests for User Story 1 (REQUIRED) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T009 [P] [US1] Add streaming behavior tests in `Tachikoma/Tests/TachikomaTests/Providers/WecodeProviderTests.swift`
- [ ] T010 [P] [US1] Add CLI runtime streaming smoke test in `Apps/CLI/Tests/CLIRuntimeTests/CLIRuntimeSmokeTests.swift`

### Implementation for User Story 1

- [ ] T011 [US1] Implement streamText flow in `Tachikoma/Sources/Tachikoma/Providers/Wecode/WecodeProvider.swift`
- [ ] T012 [US1] Add Wecode model capabilities in `Tachikoma/Sources/Tachikoma/Models/Model.swift`
- [ ] T013 [US1] Ensure agent flow routes to Wecode in `Apps/CLI/Sources/PeekabooCLI/Commands/AI/AgentCommand.swift`

**Checkpoint**: User Story 1 is functional and testable independently

---

## Phase 4: User Story 2 - Use non-streaming text with Wecode (Priority: P2)

**Goal**: Provide a combined response for non-streaming requests by aggregating the stream

**Independent Test**: Issue a non-streaming request and verify a single combined response is returned.

### Tests for User Story 2 (REQUIRED) ⚠️

- [ ] T014 [P] [US2] Add aggregation tests in `Tachikoma/Tests/TachikomaTests/Providers/WecodeProviderTests.swift`
- [ ] T015 [P] [US2] Add CLI non-streaming regression test in `Apps/CLI/Tests/CLIRuntimeTests/CLIRuntimeSmokeTests.swift`

### Implementation for User Story 2

- [ ] T016 [US2] Implement generalText aggregation in `Tachikoma/Sources/Tachikoma/Providers/Wecode/WecodeProvider.swift`
- [ ] T017 [US2] Ensure generation pipeline uses aggregation for non-streaming in `Tachikoma/Sources/Tachikoma/Core/Generation.swift`

**Checkpoint**: User Stories 1 and 2 both work independently

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Documentation and validation across stories

- [ ] T018 [P] Add provider docs in `docs/providers/wecode.md`
- [ ] T019 [P] Update provider index in `docs/providers/README.md`
- [ ] T020 Run quickstart validation steps in `specs/001-add-wecode-provider/quickstart.md`
- [ ] T021 Capture manual test notes in `specs/001-add-wecode-provider/quickstart.md`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: Depend on Foundational phase completion
- **Polish (Final Phase)**: Depends on desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational - no dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational - uses US1 streaming path but remains independently testable

### Within Each User Story

- Tests MUST be written and FAIL before implementation
- Provider wiring before CLI validation
- Story complete before moving to next priority

### Parallel Opportunities

- T003, T009, T010, T014, T015, T018, T019 can run in parallel

---

## Parallel Example: User Story 1

```bash
# Launch tests for User Story 1 together:
Task: "Add streaming behavior tests in Tachikoma/Tests/TachikomaTests/Providers/WecodeProviderTests.swift"
Task: "Add CLI runtime streaming smoke test in Apps/CLI/Tests/CLIRuntimeTests/CLIRuntimeSmokeTests.swift"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Run `peekaboo agent "hello"` with Wecode

### Incremental Delivery

1. Foundation ready → User Story 1 → validate streaming
2. Add User Story 2 → validate aggregation
3. Polish and document
