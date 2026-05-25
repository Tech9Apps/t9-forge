---
description: "8-lens code review (correctness, security, performance, design, tests, docs, conventions, dependencies) with severity-tagged structured report. Use when the user wants a deeper review than /code-review on a PR, file, or recent changes."
user-invocable: true
argument-hint: "[file|PR number]"
---

# /deep-review

8-lens code review with severity levels and structured report.

## Instructions

### 1. Gather Context

Determine scope from $ARGUMENTS:
- If a PR number: `gh pr diff` and `gh pr view`
- If a file path: `git diff` for that file
- If empty: `git diff` for all uncommitted changes

Read every changed file in full (not just the diff), related tests, and CLAUDE.md for project conventions.

### 2. Apply 8 Lenses

Review each changed file through these lenses:

1. **Clean Code + SRP** — Functions <20 lines, one responsibility, descriptive names, no dead code
2. **DRY** — Duplicated logic? Extract only if repeated 3+ times
3. **KISS** — Simpler way? Over-engineered abstractions? Unnecessary indirection?
4. **YAGNI** — Code not required by current task? Speculative features?
5. **Language Idioms** — Idiomatic patterns? Standard library used? Anti-patterns?
6. **Framework Patterns** — Correct layer? Framework conventions followed?
7. **Performance** — N+1 queries, unbounded collections, missing timeouts, non-idempotent jobs
8. **Error Handling** — No silent failures, specific error types, helpful messages, timeouts on external calls

### 3. Check Project Conventions

{{CODE_REVIEW_CONVENTIONS}}

<!-- Examples for conventions:
  - Naming conventions (camelCase, snake_case, etc.)
  - Architecture patterns (where business logic lives)
  - Required patterns (tests for new code, migrations have rollback)
  - Forbidden patterns (puts debugging, hardcoded secrets)
-->

Additional checks if reviewing a PR:
- **Diff size** — flag if >400 lines changed, suggest splitting
- **Commit hygiene** — flag single giant commit covering multiple changes
- **Destructive migrations** — flag `remove_column`, `drop_table` as BLOCKER

### 4. Structured Report

**Scope:** X files changed, Y lines added, Z lines removed

| # | Severity | Lens | File:Line | Description | Suggestion |
|---|----------|------|-----------|-------------|------------|
| 1 | BLOCKER | Performance | ... | ... | ... |
| 2 | MAJOR | Clean Code | ... | ... | ... |
| 3 | MINOR | Idioms | ... | ... | ... |
| 4 | PRAISE | DRY | ... | ... | ... |

**Severity levels:** BLOCKER → CRITICAL → MAJOR → MINOR → NIT → PRAISE

**Convention Compliance:**

| Convention | Status |
|-----------|--------|
| Tests for new code | YES/NO |
| Naming conventions | YES/NO |
| Architecture patterns | YES/NO |

**Verdict:** APPROVE / REQUEST CHANGES / NEEDS DISCUSSION

$ARGUMENTS
