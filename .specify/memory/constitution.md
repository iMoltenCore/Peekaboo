<!-- Sync Impact Report
Version change: 1.0.0 -> 1.1.0
Modified principles: N/A (initial fill)
Added sections: None (Workflow & Quality Gates expanded with stepwise commit rule)
Removed sections: None
Templates requiring updates: ✅ .specify/templates/plan-template.md, ✅ .specify/templates/tasks-template.md,
✅ .specify/templates/spec-template.md (reviewed, no changes), ⚠ .specify/templates/commands/*.md (not present)
Follow-up TODOs: TODO(RATIFICATION_DATE): original adoption date unknown
-->
# Peekaboo Constitution

## Core Principles

### I. Autonomous Execution
Work MUST proceed without waiting for user-in-the-loop feedback. Ask questions only
when blocked by missing, non-derivable inputs or by irreversible risk. Rationale:
the user is not in the loop, so momentum depends on independent execution.

### II. Minimal Change Discipline
Each change MUST be the smallest viable modification that satisfies the requirement.
Avoid scope creep and unnecessary refactors. Rationale: smaller diffs reduce risk
and preserve existing behavior.

### III. Codebase-Conformant Style
All code MUST match existing conventions, structure, and formatting for the target
module. Follow repository guidance (e.g., `AGENTS.md`) and local style tools.
Rationale: consistency preserves maintainability and reduces review friction.

### IV. Generic, Reusable Abstractions
Prefer abstractions that generalize beyond the immediate change, but only when they
reduce duplication or clarify behavior. Avoid overfitting to a single case.
Rationale: reusable components lower long-term maintenance cost.

### V. Verification and Debugging
Development MUST include appropriate testing and debugging steps for the change.
Use existing test tooling when available; if tests cannot be run, document why and
what was verified instead. Rationale: correctness is a non-negotiable outcome.

## Engineering Standards

- Follow module boundaries and conventions defined in `AGENTS.md` and `docs/`.
- Prefer typed, explicit APIs over loosely typed or ambiguous interfaces.
- Do not introduce secrets, credentials, or environment-specific data into the repo.

## Workflow & Quality Gates

- Confirm scope and constraints from the spec or issue before editing code.
- Implement the minimal change first, then improve for clarity and reuse if needed.
- Work step by step and commit each completed step to version control.
- Run the most relevant tests or diagnostics; record any gaps and rationale.
- Update documentation when behavior, flags, or usage changes.

## Governance

- This constitution supersedes conflicting project practices and templates.
- Amendments require a documented rationale, a semantic version bump, and an
  explicit note of any behavior or process changes.
- Compliance MUST be verified during planning (Constitution Check) and during
  review for any delivery artifact (specs, plans, tasks, or code).
- The amendment process is change by pull request or tracked change request with
  reviewer acknowledgement.

**Version**: 1.1.0 | **Ratified**: TODO(RATIFICATION_DATE): original adoption date unknown | **Last Amended**: 2026-02-03
