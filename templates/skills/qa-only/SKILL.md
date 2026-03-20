# /qa-only

Run QA in report-only mode with no code changes.

## Instructions

### 1. Scope
- Use provided URL and/or branch diff context.
- Prioritize critical user paths and changed surfaces.

### 2. Capability gate
- Requires browser automation runtime.
- If unavailable, provide a manual test plan and identify what could not be executed.

### 3. Execute report-only testing
- Reproduce flows.
- Capture evidence (screenshots/log signals) for failures.
- Do not edit files or apply patches.

### 4. Output
- Severity-ranked findings.
- Reproduction steps.
- Risk summary and recommended fix sequence.

$ARGUMENTS
