<!--
Sync Impact Report
- Version change: template -> 1.0.0
- Modified principles: N/A (initial adoption)
- Added sections: Core Principles, Quality Standards, Workflow & Review, Governance
- Removed sections: None
- Templates requiring updates:
  - ✅ .specify/templates/plan-template.md
  - ✅ .specify/templates/tasks-template.md
  - ⚠ .specify/templates/commands/*.md (directory not present)
- Follow-up TODOs:
  - TODO(RATIFICATION_DATE): original ratification date unknown
-->
# Peekaboo Constitution

## Core Principles

### I. Code Quality and Readability
All production code MUST be explicit, readable, and maintainable. Changes MUST
follow formatting and lint rules, avoid hidden side effects, and keep complexity
bounded. If a change increases complexity, it MUST be justified and documented.

### II. Testing Discipline (Non-Negotiable)
Every functional change MUST include tests at the appropriate level (unit,
integration, contract, or automation). Tests MUST be deterministic and runnable
in CI. If a required test cannot be added, a written waiver with rationale and
risk assessment MUST be included in the plan and review notes.

### III. API Design and Generic Contracts
Public APIs MUST be stable, minimal, and explicit about inputs, outputs, and
errors. APIs SHOULD be generic over callers and platforms, avoiding leakage of
implementation details. Breaking changes require explicit versioning and
migration guidance.

### IV. Reviewable and Traceable Changes
Each change MUST be small enough to review and trace to a requirement. Refactors
must be scoped to the feature at hand unless explicitly approved. Documentation
and examples MUST be updated when behavior changes.

### V. Quality Gates Before Merge
All required checks MUST pass before merging: formatting, linting, tests, and
any documented performance or permission checks. Known failures are not
acceptable without a documented waiver.

## Quality Standards

- Formatting and linting MUST be clean (SwiftFormat, SwiftLint, or project
  equivalents) before review.
- Explicit `self` and typed APIs are required; avoid `Any` unless documented.
- Error paths MUST be explicit and covered by tests where feasible.
- Public surfaces MUST include clear naming and minimal, consistent signatures.

## Workflow & Review

- Plans MUST enumerate testing scope and identify API changes up front.
- Reviews MUST verify compliance with all Core Principles and note any waivers.
- API changes MUST include compatibility notes, deprecation paths, or version
  bumps.
- Work that cannot meet the standards MUST be deferred or explicitly approved.

## Governance

- This constitution supersedes local conventions and feature requests.
- Amendments require a version bump, a recorded rationale, and an impact report.
- Compliance is reviewed during specification, planning, and code review.
- Versioning follows semantic rules: MAJOR for breaking changes, MINOR for new
  principles or material expansions, PATCH for clarifications.

**Version**: 1.0.0 | **Ratified**: TODO(RATIFICATION_DATE): original adoption date unknown | **Last Amended**: 2026-01-30
