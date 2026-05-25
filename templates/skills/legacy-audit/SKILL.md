---
description: "Read-only audit of a codebase for modernization opportunities: dependency age, dead code, complexity hotspots, test coverage gaps. Use when planning a refactor or assessing tech debt."
user-invocable: true
argument-hint: "[deps|dead-code|complexity|coverage]"
---

# /legacy-audit

Audit a codebase for modernization opportunities: dependency age, dead code, complexity hotspots, test coverage gaps.

This is a read-only audit. No files will be modified.

## Instructions

If $ARGUMENTS specifies a scope (`deps`, `dead-code`, `complexity`, `coverage`), run only that phase. Otherwise run all.

### 1. Dependency Age Audit

Check dependency freshness:

```
{{DEPENDENCY_CHECK_COMMAND}}
```

<!-- Examples for common stacks:
  Node/TypeScript: npm outdated
  Python: pip list --outdated
  Ruby: bundle outdated --strict
  Go: go list -m -u all
  Elixir: mix hex.outdated
  Rust: cargo outdated
-->

Classify each outdated dependency:

| Category | Definition | Action |
|----------|-----------|--------|
| CRITICAL | 2+ major versions behind OR known CVEs | Upgrade immediately |
| STALE | 1 major version behind | Plan upgrade |
| AGING | Minor/patch versions behind | Upgrade when convenient |
| CURRENT | Up to date | No action |

Run security scan:

```
{{SECURITY_AUDIT_COMMAND}}
```

<!-- Examples for common stacks:
  Node/TypeScript: npm audit
  Python: pip-audit
  Ruby: bundle audit check
  Go: govulncheck ./...
  Elixir: mix hex.audit
  Rust: cargo audit
-->

### 2. Dead Code Detection

Search for:
1. Unused files — not imported/required anywhere
2. Unused functions/methods — defined but never called
3. Commented-out code blocks longer than 5 lines
4. Dead routes — pointing to missing controllers/handlers
5. Unused dependencies — in lockfile but not imported in source

Report: `| File:Line | Type | Evidence | Safe to Remove? |`

### 3. Complexity Hotspots

Identify:
1. Large files — over 300 lines (sort by size)
2. God classes — 10+ public methods
3. Long methods — over 50 lines
4. Deep nesting — 4+ levels of indentation
5. High churn + high complexity — cross-reference with git history

```bash
git log --format="%H" --since="6 months ago" -- <file> | wc -l
```

Report: `| File:Line | Metric | Value | Risk | Suggested Action |`

### 4. Test Coverage Gaps

1. Source files with no corresponding test file
2. Test files not updated in 6+ months (stale tests)
3. Critical paths missing integration tests
4. Run coverage tool if available:

```
{{COVERAGE_COMMAND}}
```

<!-- Examples for common stacks:
  Node/TypeScript: npx vitest --coverage OR npx jest --coverage
  Python: pytest --cov
  Ruby: COVERAGE=true bundle exec rspec
  Go: go test -coverprofile=coverage.out ./...
-->

### 5. Summary Report

```
Legacy Audit Report
===================

Dependency Health:  X CRITICAL / Y STALE / Z AGING / W CURRENT
Security Issues:    X vulnerabilities found
Dead Code:          X files / Y functions / Z commented blocks
Complexity:         X hotspots (high churn + high complexity)
Test Coverage:      X source files with no test / Y stale tests

Top 5 Modernization Priorities:
1. [highest impact item]
2. ...

Estimated Effort: [small/medium/large] per priority
```

$ARGUMENTS
