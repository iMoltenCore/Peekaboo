# Implementation Plan: Add Wecode Provider

**Branch**: `001-add-wecode-provider` | **Date**: 2026-02-03 | **Spec**: specs/001-add-wecode-provider/spec.md
**Input**: Feature specification from `specs/001-add-wecode-provider/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Add a Wecode provider for Peekaboo text generation with streaming output and a
non-streaming path that aggregates streamed content into a single response.

## Technical Context

<!--
  ACTION REQUIRED: Replace the content in this section with the technical details
  for the project. The structure here is presented in advisory capacity to guide
  the iteration process.
-->

**Language/Version**: Swift 6.2  
**Primary Dependencies**: Tachikoma (provider framework), Commander (CLI), PeekabooCore  
**Storage**: N/A (reuse existing config storage)  
**Testing**: Swift Testing/XCTest (existing CLI and Tachikoma test suites)  
**Target Platform**: macOS 15+ CLI
**Project Type**: Single repo with SwiftPM modules (CLI + Core + Tachikoma)  
**Performance Goals**: First streamed content within ~2s for typical prompts; no regression vs current providers  
**Constraints**: Must run `peekaboo agent "hello"` with Wecode; no user-in-loop required; no secrets in repo  
**Scale/Scope**: Add one provider integration and wiring in provider selection paths

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
Apps/CLI/Sources/PeekabooCLI/
├── Commands/
├── CLI/
└── Helpers/

Core/PeekabooCore/Sources/PeekabooAgentRuntime/

Tachikoma/Sources/Tachikoma/
├── Core/
└── Providers/

Apps/CLI/Tests/
Tachikoma/Tests/
```

**Structure Decision**: SwiftPM modules within the monorepo; provider work lives
in `Tachikoma/Sources/Tachikoma/Providers` with CLI integration under
`Apps/CLI/Sources/PeekabooCLI`.

## Constitution Check (Post-Design)

- Autonomous Execution: No user-in-loop steps required.
- Minimal Change Discipline: Changes scoped to provider integration and wiring.
- Codebase-Conformant Style: Changes confined to existing Swift modules.
- Generic, Reusable Abstractions: Aggregation logic reusable for stream-only providers.
- Verification and Debugging: Manual CLI validation planned for `peekaboo agent "hello"`.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |
