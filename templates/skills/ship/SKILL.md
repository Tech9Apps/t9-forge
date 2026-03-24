# /ship

Execute release hygiene for a ready branch and open/update the PR.

## Instructions

### 1. Validate branch readiness
- Confirm clean/expected branch state.
- Confirm base branch and divergence.
- Summarize commits since base branch.
- Identify high-risk areas (auth, payments, migrations, infra).

### 2. Run verification chain
- Build: `{{BUILD_COMMAND}}`
- Lint: `{{LINT_COMMAND}}`
- Typecheck: `{{TYPECHECK_COMMAND}}`
- Tests: `{{TEST_ALL_COMMAND}}`

### 3. Check operational readiness
- Config/env assumptions documented.
- Migration requirements identified.
- Rollback path identified.

### 4. Handle review backlog
- Resolve blocking findings from `/code-review` or `/deep-review`.
- If GitHub tooling is unavailable, run local-only release checks and report limitation.

### 5. Release actions
- Sync with base branch strategy.
- Push branch.
- Create/update PR when supported.
- If `--dry-run` is specified, stop here and output assessment without pushing.

### 6. Output
- Final status (`SHIPPED`, `READY TO MERGE`, `BLOCKED`, or `NOT READY` for dry-run).
- Remaining blockers (numbered) and exact next command.
- Suggested remediation sequence for any blockers.

$ARGUMENTS
