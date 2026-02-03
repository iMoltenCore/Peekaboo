# Implementation Plan: Add Wecode Provider

**Branch**: `001-add-wecode-provider` | **Date**: 2026-02-03 | **Spec**: specs/001-add-wecode-provider/spec.md
**Input**: Feature specification from `specs/001-add-wecode-provider/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Add Wecode as a selectable provider that streams text output and supports
non-streaming text by aggregating stream chunks, aligning behavior with existing
stream-first providers while preserving current workflows.

## Technical Context

<!--
  ACTION REQUIRED: Replace the content in this section with the technical details
  for the project. The structure here is presented in advisory capacity to guide
  the iteration process.
-->

**Language/Version**: Swift 6.2  
**Primary Dependencies**: Tachikoma provider framework, Foundation  
**Storage**: N/A  
**Testing**: XCTest (SwiftPM)  
**Target Platform**: macOS  
**Project Type**: Multi-module SwiftPM + apps  
**Performance Goals**: 95% of streams deliver first text within 2 seconds  
**Constraints**: Wecode does not support non-streaming text directly; aggregate
streamed output for non-streaming requests without new auth flows  
**Scale/Scope**: Provider integration and selection path only (no new UX flows)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- Autonomous Execution: plan does not require user-in-loop approvals to proceed.
- Minimal Change Discipline: scope stays at the smallest viable change set.
- Codebase-Conformant Style: plan references existing structure and style tooling.
- Generic, Reusable Abstractions: design avoids one-off solutions when reuse helps.
- Verification and Debugging: test/debug steps are identified or gaps are justified.

## Project Structure

### Documentation (this feature)

```text
specs/[###-feature]/
├── plan.md              # This file (/speckit.plan command output)
├── research.md          # Phase 0 output (/speckit.plan command)
├── data-model.md        # Phase 1 output (/speckit.plan command)
├── quickstart.md        # Phase 1 output (/speckit.plan command)
├── contracts/           # Phase 1 output (/speckit.plan command)
└── tasks.md             # Phase 2 output (/speckit.tasks command - NOT created by /speckit.plan)
```

### Source Code (repository root)
<!--
  ACTION REQUIRED: Replace the placeholder tree below with the concrete layout
  for this feature. Delete unused options and expand the chosen structure with
  real paths (e.g., apps/admin, packages/something). The delivered plan must
  not include Option labels.
-->

```text
Tachikoma/
├── Sources/Tachikoma/Providers/
│   ├── ProviderFactory.swift
│   ├── OpenAI/OpenAIResponsesProvider.swift
│   └── Wecode/WecodeProvider.swift
└── Sources/Tachikoma/Core/
    └── Generation.swift

Tachikoma/Tests/TachikomaTests/Providers/
```

**Structure Decision**: Provider integration lives in Tachikoma provider sources
and related tests under Tachikoma tests.

## Phase 0: Research

- Confirm Wecode stream-to-text aggregation behavior needed for non-streaming use.
- Identify existing provider patterns that convert streams to single responses.

## Phase 1: Design & Contracts

- Document data model entities for provider config, stream chunks, and combined output.
- Define internal contracts for streaming and aggregated text expectations.
- Draft quickstart updates describing Wecode selection and expected behavior.

## Phase 2: Planning

- Translate design into concrete tasks for provider implementation and tests.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |
