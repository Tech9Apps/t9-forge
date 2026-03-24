# /qa

Quality assurance with two paths: **browser-backed** when automation is available (runtime evidence); **structured test authoring** (5-phase) when the task is codebase/test-suite focused or the browser runtime is unavailable.

Pick **Path A** when browser automation is present and you need interactive or URL-based verification. Pick **Path B** when you are driving coverage and specs from diffs without a browser, or after Path A’s capability gate fails (treat Path B as the substantive fallback instead of an empty report).

---

## Path A — Browser-backed QA

### 1. Determine mode
- Diff-aware mode if on feature branch.
- URL mode if environment URL is provided.
- `--quick` for smoke checks.

### 2. Capability gate
- Requires browser automation runtime.
- If session cookies are needed for authenticated flows, import them first (never print cookie values; report only domain-level import counts).
- If `--report-only` is specified, execute checks but do not edit files or apply patches — output findings only.
- If browser automation is unavailable, switch to **Path B**.

### 3. Build test scope
- Identify changed routes/pages from git diff when possible.
- Include adjacent regression paths likely impacted by changes.

### 4. Execute checks
- Navigate through target flows.
- Validate form behavior and key interactions.
- Capture screenshots for defects.
- Check runtime errors.

### 5. Output
- Health score + severity-ranked issues.
- Reproduction steps and suggested fix order.
- If fixes are applied, include before/after verification notes.

---

## Path B — Structured test authoring (5 phases)

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
