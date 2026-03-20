# /qa-design-review

Run a design audit and apply targeted styling fixes with verification.

## Instructions

### 1. Start with design audit
- Produce same scoring baseline as `/plan-design-review`.
- Prioritize high-impact fixes first.

### 2. Capability gate
- Requires browser automation evidence loop.
- If unavailable, provide report-only design findings and suggested patch plan.

### 3. Apply minimal fixes
- Prefer CSS/style-layer fixes before component logic changes.
- Keep each fix isolated and reversible.

### 4. Verify each fix
- Re-check affected view.
- Capture before/after evidence.
- Stop if risk grows beyond agreed threshold.

### 5. Output
- Score deltas.
- Applied fixes and deferred items.
- Residual design risk.

$ARGUMENTS
