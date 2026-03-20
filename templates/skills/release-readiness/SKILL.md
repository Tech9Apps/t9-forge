# /release-readiness

Assess whether the current branch is safe to release.

## Instructions

### 1. Verify branch scope
- Summarize commits since base branch
- Identify high-risk areas (auth, payments, migrations, infra)

### 2. Run verification chain
- Build: `{{BUILD_COMMAND}}`
- Lint: `{{LINT_COMMAND}}`
- Typecheck (if applicable): `{{TYPECHECK_COMMAND}}`
- Tests: `{{TEST_ALL_COMMAND}}`

### 3. Check operational readiness
- Config/env assumptions documented
- Migration requirements identified
- Rollback path identified

### 4. Output status
- `READY` or `NOT READY`
- Blocking issues (numbered)
- Suggested remediation sequence

$ARGUMENTS
