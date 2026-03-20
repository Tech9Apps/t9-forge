# /plan-eng-review

Convert an approved product direction into a buildable technical plan.

## Instructions

### 1. Define architecture and boundaries
- Identify services/modules involved.
- Define trust boundaries and ownership per component.
- Identify sync vs async execution points.

### 2. Model state and failure paths
- List core state transitions.
- Cover retries, idempotency, and partial failure handling.
- Identify race/concurrency hazards.

### 3. Define verification strategy
- Unit checks for core logic.
- Integration checks for boundaries and contracts.
- End-to-end checks for critical flows.

### 4. Produce implementation plan
- Max 10 numbered tasks.
- Each task must include files, risk notes, and verification commands.
- Include rollout and rollback notes for risky changes.

### 5. Handoff
- Ask whether to proceed to implementation.

Planning only. Do not modify code from this skill.

$ARGUMENTS
