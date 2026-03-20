# Browse Status

Show browser-automation readiness and recent browse activity.

## Instructions

Run the following checks and summarize:

### Runtime capability
```bash
{{CI_STATUS_COMMAND}}
```

### Recent activity hints
```bash
git log --oneline -5
```

### Summary
- Browser automation available/unavailable
- If unavailable, explicit missing prerequisite
- Recommended next command

$ARGUMENTS
