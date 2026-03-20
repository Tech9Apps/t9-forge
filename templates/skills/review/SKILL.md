# /review

Perform a high-rigor, production-risk-oriented code review.

## Instructions

### 1. Determine review scope
- Prefer branch diff against default branch.
- If arguments specify files/PR, scope to that input.

### 2. Analyze by failure mode
- Correctness/invariant violations.
- Concurrency/race conditions.
- Security/trust boundary flaws.
- Performance and scalability hazards.
- Missing tests for real failure paths.

### 3. Greptile-aware behavior (if available)
- Triage external review comments into: valid, already-fixed, false-positive.
- Include link/context in findings when available.

### 4. Report structure
- Order by severity (`Critical`, `High`, `Medium`, `Low`).
- For each issue include: evidence, impact, and concrete fix direction.
- End with clear `Ship decision`: `READY`, `READY WITH FIXES`, or `NOT READY`.

### 5. If no findings
- Explicitly state no critical findings and list residual risk.

$ARGUMENTS
