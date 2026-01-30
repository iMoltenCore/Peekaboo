---
name: "ios-library-analysis"
description: "Use when analyzing iOS system or private libraries, especially to map symbols to source, compare versions, or extract frameworks from firmware."
compatibility: "opencode"
metadata:
  workflow: "Identify library -> map to Apple OSS -> extract symbols -> compare versions -> validate behavior in binaries"
---

# iOS Library Analysis

## Overview
Analyze iOS system or private libraries by mapping binary symbols to Apple OSS sources, extracting framework artifacts, and comparing versions to explain behavior changes.

## When to Use
- Investigating undocumented system frameworks or private APIs.
- Mapping symbols and behaviors to Apple OSS sources.
- Comparing library versions across iOS releases.

## Workflow
1. Identify the library/framework and target iOS version.
2. Map the library to Apple OSS sources in `apple-oss-distributions`.
3. Extract symbols and headers for comparison.
4. Compare versions to detect behavior changes.
5. Validate findings with binary inspection.

## Requirements
- Use Apple OSS references from `apple-oss-distributions` during analysis.
- For firmware or private framework extraction, reference the `ipsw` skill.
- Call out related analysis skills when they apply: `binary-triage`, `deep-analysis`, `idapython`.

## Scripts
- `scripts/oss_symbol_search.py`: Search OSS sources for symbol names. Run: `python scripts/oss_symbol_search.py <oss-root> <symbol>`.
- `scripts/compare_headers.py`: Compare headers to list added or removed declarations. Run: `python scripts/compare_headers.py <old.h> <new.h>`.

## Resources
- `resources/apple-oss-references.md`
- `resources/library-analysis-checklist.md`
- `resources/ipsw-workflows.md`
