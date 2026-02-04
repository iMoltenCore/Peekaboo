# Implementation Plan: Add Wecode Provider

**Branch**: `001-add-wecode-provider` | **Date**: 2026-02-03 | **Spec**: specs/001-add-wecode-provider/spec.md
**Input**: Feature specification from `/specs/001-add-wecode-provider/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Add Wecode as a selectable provider for text generation with streaming support, and
support non-streaming requests by aggregating streamed content into a single
response.

## Technical Context

<!--
  ACTION REQUIRED: Replace the content in this section with the technical details
  for the project. The structure here is presented in advisory capacity to guide
  the iteration process.
-->

**Language/Version**: Swift 6.2  
**Primary Dependencies**: Tachikoma, Commander, PeekabooCore  
**Storage**: N/A  
**Testing**: XCTest (Tachikoma tests)  
**Target Platform**: macOS 13+ (CLI and mac app), iOS 16+ compatibility for provider layer  
**Project Type**: Multi-module Swift workspace (CLI + mac app + shared core)  
**Performance Goals**: First streamed text within 2 seconds for 95% of requests  
**Constraints**: Streaming must preserve order; non-streaming aggregation must not lose content  
**Scale/Scope**: Single provider addition, minimal changes to existing provider selection

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
Apps/CLI/
├── Sources/
└── Tests/

Core/PeekabooCore/

Tachikoma/
├── Sources/
│   └── Tachikoma/
│       ├── Core/
│       └── Providers/
│           ├── OpenAI/
│           └── Wecode/
└── Tests/
```

**Structure Decision**: Provider implementation lives in `Tachikoma` with shared
core behavior in `Tachikoma/Sources/Tachikoma/Core`; selection flows are wired
through provider factory in `Tachikoma/Sources/Tachikoma/Providers`.

## Phase 0: Outline & Research

- Review existing provider patterns (especially `OpenAIResponsesProvider`) and
  current Wecode stub.
- Confirm how non-streaming requests are represented in the provider interface.

## Phase 1: Design & Contracts

- Define data model for stream chunks and combined responses.
- Produce a lightweight API contract for streaming and aggregated text.
- Draft quickstart guidance for enabling Wecode in existing flows.
- Update agent context with new provider details.

## Phase 1: Constitution Re-check

- Autonomous Execution: No user-in-loop dependencies required.
- Minimal Change Discipline: Add provider implementation and wiring only.
- Codebase-Conformant Style: Follow Swift and Tachikoma conventions.
- Generic, Reusable Abstractions: Prefer shared streaming aggregation utility if needed.
- Verification and Debugging: Add or update provider tests where applicable.

## Phase 2: Planning

- Break implementation into tasks after research and design outputs are complete.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |
