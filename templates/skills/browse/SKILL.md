# /browse

Use browser automation to inspect and validate live UI behavior.

## Instructions

### 1. Capability gate
- If browser automation is unavailable, switch to report-only mode and explain the missing capability.
- For Cursor targets, use the target browser tooling path rather than Claude-only shell assumptions.

### 2. Execute focused browser checks
- Navigate to provided URL(s).
- Validate key page state and flows.
- Capture screenshot evidence for failures.
- Check console/network error signals when available.

### 3. Report
- Pages/flows tested.
- Pass/fail summary.
- Defects with reproduction steps and evidence.

### 4. Output style
- Keep output concise and evidence-led.
- Do not claim a check passed without runtime evidence.

$ARGUMENTS
