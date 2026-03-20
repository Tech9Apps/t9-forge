# /qa

Run QA with runtime evidence, and optionally apply fixes when requested.

## Instructions

### 1. Determine mode
- Diff-aware mode if on feature branch.
- URL mode if environment URL is provided.
- `--quick` for smoke checks.

### 2. Capability gate
- Requires browser automation runtime.
- If unavailable, downgrade to report-only QA plan and clearly flag missing capabilities.

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

$ARGUMENTS
