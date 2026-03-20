# QA Status

Show QA readiness and latest verification posture.

## Instructions

Run and summarize:

### Branch context
```bash
git status --short --branch
git log --oneline -10
```

### Verification baseline
```bash
{{VERIFY_COMMAND}}
```

### Summary
- QA readiness (ready / blocked)
- Known blockers
- Suggested next QA mode (`/qa`, `/qa --quick`, `/qa-only`)

$ARGUMENTS
