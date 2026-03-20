# Design Audit Status

Summarize design-review readiness and current UI quality signals.

## Instructions

### Gather baseline
```bash
git status --short --branch
```

### Build/test safety check
```bash
{{TEST_COMMAND}}
```

### Summary
- Whether design audit can be run now
- Surfaces likely impacted by current diff
- Suggested next step (`/plan-design-review` or `/qa-design-review`)

$ARGUMENTS
