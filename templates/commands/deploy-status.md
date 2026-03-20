# Deploy Status

Show deployment and CI status relevant to this repository.

## Instructions

Run the following in order and present a concise summary.

### 1. Show CI status
```bash
{{CI_STATUS_COMMAND}}
```

### 2. Show latest release/deploy details
```bash
{{DEPLOY_STATUS_COMMAND}}
```

### 3. Summarize
- Latest deploy target/environment
- Current status (healthy/degraded/failed)
- Most recent failure signal (if any)

If one command is unavailable in this repo, report that explicitly and continue with available signals.

$ARGUMENTS
