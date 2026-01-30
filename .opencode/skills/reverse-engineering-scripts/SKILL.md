---
name: "reverse-engineering-scripts"
description: "Use when building or refactoring Python and JS/TS automation scripts for reverse-engineering workflows, especially when repeatable tooling is needed."
compatibility: "opencode"
metadata:
  workflow: "Define task -> choose Python or JS/TS -> scaffold with uv/bun -> implement -> document entry points"
---

# Reverse Engineering Scripts

## Overview
Build small, reusable automation scripts for analysis tasks. Prefer clear entry points, minimal dependencies, and repeatable outputs.

## When to Use
- Repeating manual RE steps or data extraction.
- Need to standardize a workflow across binaries or versions.
- Lightweight automation without full application overhead.

## Workflow
1. Define the input/output contract.
2. Choose Python or JS/TS based on ecosystem fit.
3. Use `uv` for Python environments and `bun` for JS/TS.
4. Implement and document entry points.
5. Keep scripts small and composable.

## Scripts
- `scripts/extract_strings.py`: Extract ASCII strings from binaries. Run: `uv run python scripts/extract_strings.py --file <path>`.
- `scripts/extract_strings.ts`: TypeScript variant for quick usage with bun. Run: `bun run scripts/extract_strings.ts --file <path>`.

## Resources
- `resources/python-uv-notes.md`
- `resources/bun-notes.md`
- `resources/automation-libs.md`
