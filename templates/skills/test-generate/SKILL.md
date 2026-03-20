# /test-generate

Generate or improve tests for changed behavior and uncovered risk paths.

## Instructions

### 1. Identify change scope
- Inspect staged and unstaged file changes
- Map changed production files to likely test locations

### 2. Detect available test layers
- Unit, integration, e2e
- If a layer does not exist in this project, skip it

### 3. Add tests with priority
- Failure-path and edge-case coverage first
- Then happy-path coverage

### 4. Keep tests explicit
- Strong assertions on behavior, errors, and side effects
- Avoid weak "does not throw" style tests where stronger checks are possible

### 5. Run project test commands
- Focused tests first: `{{TEST_COMMAND}}`
- Full suite if needed: `{{TEST_ALL_COMMAND}}`

### 6. Report
- What tests were added/updated
- Which layers were skipped and why
- Remaining risk areas

$ARGUMENTS
