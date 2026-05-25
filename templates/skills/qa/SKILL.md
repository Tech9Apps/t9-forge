---
description: "5-phase QA workflow — reconnaissance, probing questions, test plan, spec writing, execution. Use when the user wants thorough quality assurance on a change, a comprehensive test plan, or rigorous validation before shipping."
user-invocable: true
argument-hint: "[file|module]"
---

# /qa

5-phase quality assurance workflow: reconnaissance, probing questions, test plan, spec writing, execution.

## Instructions

### 1. Reconnaissance

Identify changed files and classify by risk:

```bash
git diff --name-only HEAD~1
```

If $ARGUMENTS specifies a file or module, scope to that instead.

**Risk classification:**
- **CRITICAL** — auth, payments, data models, shared utilities, API endpoints
- **HIGH** — business logic, services, controllers
- **MEDIUM** — views, serializers, helpers, config
- **LOW** — docs, comments, formatting

Read each changed file and its existing tests. Build a context table:

| File | Type | Risk | Existing Tests? |
|------|------|------|----------------|

### 2. Probing Questions

Before writing any tests, ask 3-8 targeted questions about risk and intent. Group them — don't ask one at a time.

**Good questions** (risk-focused):
- "This touches the payment flow — should I test refund edge cases?"
- "The new validation rejects blank input. What about unicode-only strings?"
- "This service calls an external API — should I mock it or test integration?"

Do NOT ask what the code does (read it), whether to write tests (yes), or what framework to use (detect it).

### 3. Test Plan

Present a structured test plan BEFORE writing specs. Organize by category:

| # | Category | Test Description | Risk Level |
|---|----------|-----------------|------------|
| 1 | Happy Path | Expected inputs produce expected outputs | ... |
| 2 | Edge Cases | Boundary values, empty inputs, nil/null | ... |
| 3 | Error Cases | Invalid input, network failures, timeouts | ... |
| 4 | Adversarial | Injection strings, script tags, huge inputs | ... |
| 5 | Performance | N+1 queries, unbounded collections (CRITICAL/HIGH only) | ... |

Wait for user approval before proceeding.

### 4. Write Specs

Write tests using the project's test framework:

```
{{TEST_COMMAND}}
```

<!-- Examples for common stacks:
  Node/TypeScript: npx jest, npx vitest
  Python: pytest
  Ruby: bundle exec rspec
  Go: go test ./...
  Elixir: mix test
-->

**Test quality rules:**
- One assertion per test (when practical)
- Descriptive names — `it "returns 404 when record not found"` not `it "works"`
- Arrange-Act-Assert structure
- All test data visible in the test (no mystery guests)
- Test behavior, not implementation

### 5. Execute and Report

1. Run the new specs (targeted)
2. Fix any failures — read error, read source, fix root cause
3. Run the full suite to check for regressions: `{{TEST_ALL_COMMAND}}`

<!-- Examples for common stacks:
  Node/TypeScript: npm test
  Python: pytest
  Ruby: bundle exec rspec
  Go: go test ./...
  Elixir: mix test
-->

**QA Report:**

| File | Tests Added | Coverage |
|------|------------|----------|
| ... | ... | ... |

| # | Severity | Description | Status |
|---|----------|-------------|--------|
| 1 | CRITICAL | ... | FIXED/OPEN |

| Check | Status |
|-------|--------|
| Security (no injection, XSS, CSRF) | PASS/WARN/FAIL |
| Performance (no N+1, bounded queries) | PASS/WARN/FAIL |
| Error handling (no silent failures) | PASS/WARN/FAIL |
| Data integrity (validations, constraints) | PASS/WARN/FAIL |

**Verdict:** SHIP IT / FIX AND RE-TEST / NEEDS REWORK

$ARGUMENTS
