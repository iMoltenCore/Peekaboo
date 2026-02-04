---

description: "Tasks for Add Wecode Provider"
---

# Tasks: Add Wecode Provider

**Input**: Design documents from `/specs/001-add-wecode-provider/`
**Prerequisites**: plan.md (required), spec.md (required), research.md, data-model.md, contracts/

**Tests**: Tests are REQUIRED unless explicitly waived in the specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Verify Wecode provider scaffolding exists in Tachikoma/Sources/Tachikoma/Providers/Wecode/WecodeProvider.swift
- [x] T002 [P] Review provider selection flow in Tachikoma/Sources/Tachikoma/Providers/ProviderFactory.swift
- [x] T003 [P] Review stream delta conventions in Tachikoma/Sources/Tachikoma/Core/Types.swift

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T004 Define Wecode model identifiers in Tachikoma/Sources/Tachikoma/Models/LanguageModel.swift
- [x] T005 [P] Register Wecode in provider selection flow in Tachikoma/Sources/Tachikoma/Providers/ProviderFactory.swift
- [x] T006 [P] Confirm provider configuration keys in Tachikoma/Sources/Tachikoma/Configuration/TachikomaConfiguration.swift

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Stream text with Wecode (Priority: P1) 🎯 MVP

**Goal**: Support streaming text output when Wecode is selected.

**Independent Test**: Issue a streaming text request and observe incremental output.

### Tests for User Story 1 (REQUIRED unless explicitly waived) ⚠️

- [x] T007 [P] [US1] Add streamText test coverage in Tachikoma/Tests/TachikomaTests/Providers/WecodeProviderTests.swift
- [x] T008 [P] [US1] Add provider selection test in Tachikoma/Tests/TachikomaTests/Providers/ProviderFactoryTests.swift

### Implementation for User Story 1

- [x] T009 [US1] Implement Wecode streamText in Tachikoma/Sources/Tachikoma/Providers/Wecode/WecodeProvider.swift
- [x] T010 [US1] Add Wecode request/response models in Tachikoma/Sources/Tachikoma/Providers/Wecode/
- [x] T011 [US1] Add streaming parser in Tachikoma/Sources/Tachikoma/Providers/Wecode/

**Checkpoint**: User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Use non-streaming text with Wecode (Priority: P2)

**Goal**: Support non-streaming text requests by aggregating stream output.

**Independent Test**: Issue a non-streaming request and receive a single combined response.

### Tests for User Story 2 (REQUIRED unless explicitly waived) ⚠️

- [x] T012 [P] [US2] Add generateText aggregation tests in Tachikoma/Tests/TachikomaTests/Providers/WecodeProviderTests.swift
- [x] T013 [P] [US2] Add edge case tests for empty/failed stream in Tachikoma/Tests/TachikomaTests/Providers/WecodeProviderTests.swift

### Implementation for User Story 2

- [x] T014 [US2] Implement Wecode generateText aggregation in Tachikoma/Sources/Tachikoma/Providers/Wecode/WecodeProvider.swift
- [x] T015 [US2] Ensure finishReason and usage handling in Tachikoma/Sources/Tachikoma/Providers/Wecode/WecodeProvider.swift

**Checkpoint**: User Story 2 should be functional and testable independently

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T016 [P] Update provider documentation in docs/ (add Wecode notes)
- [x] T017 [P] Run unit tests for Tachikoma providers in Tachikoma/Tests/
- [ ] T018 Run `peekaboo agent "hello"` as the final verification step

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Depends on US1 stream implementation

### Within Each User Story

- Tests MUST be written and fail before implementation
- Stream implementation before aggregation
- Story complete before moving to next priority

### Parallel Opportunities

- T002 and T003 can run in parallel
- T007 and T008 can run in parallel
- T012 and T013 can run in parallel

---

## Parallel Example: User Story 1

```bash
# Launch tests for User Story 1 together:
Task: "Add streamText test coverage in Tachikoma/Tests/TachikomaTests/Providers/WecodeProviderTests.swift"
Task: "Add provider selection test in Tachikoma/Tests/TachikomaTests/Providers/ProviderFactoryTests.swift"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test streaming independently

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Validate streaming
3. Add User Story 2 → Test independently → Validate aggregation
4. Run final verification `peekaboo agent "hello"`

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
