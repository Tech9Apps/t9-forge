# /ship

Execute release hygiene for a ready branch and open/update the PR.

## Instructions

### 1. Validate branch readiness
- Confirm clean/expected branch state.
- Confirm base branch and divergence.
- Confirm release scope from commits.

### 2. Run verification chain
- Build: `{{BUILD_COMMAND}}`
- Lint: `{{LINT_COMMAND}}`
- Typecheck: `{{TYPECHECK_COMMAND}}`
- Tests: `{{TEST_ALL_COMMAND}}`

### 3. Handle review backlog
- Resolve blocking findings from `/review`.
- If GitHub tooling is unavailable, run local-only release checks and report limitation.

### 4. Release actions
- Sync with base branch strategy.
- Push branch.
- Create/update PR when supported.

### 5. Output
- Final status (`SHIPPED`, `READY TO MERGE`, `BLOCKED`).
- Remaining blockers and exact next command.

$ARGUMENTS
