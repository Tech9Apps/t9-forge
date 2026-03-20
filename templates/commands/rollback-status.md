# Rollback Status

Show rollback readiness and available rollback actions.

## Instructions

Run the following in order and present rollback readiness.

### 1. Inspect current release metadata
```bash
{{DEPLOY_STATUS_COMMAND}}
```

### 2. Inspect rollback capability
```bash
{{ROLLBACK_STATUS_COMMAND}}
```

### 3. Summarize
- Whether rollback is currently possible
- Rollback method (image/tag/revision/database strategy)
- Required manual steps and risks

If rollback data is incomplete, call out missing prerequisites explicitly.

$ARGUMENTS
