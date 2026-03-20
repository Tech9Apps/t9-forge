# /plan

Create an execution-ready implementation plan for the requested change.

## Instructions

Follow this workflow:

### 1. Clarify scope
- Confirm desired outcome
- Confirm constraints and non-goals
- Confirm risk tolerance and timeline

### 2. Analyze codebase
- Identify touched modules and dependencies
- Identify data flow and side effects
- Identify verification requirements

### 3. Produce numbered tasks
- Each task should be one clear unit of work
- Include exact files expected to change
- Include verification commands per task
- Include rollback/recovery notes for risky steps

### 4. Keep output concise
- Max 8 tasks unless user requests more detail
- Prefer explicit steps over abstract guidance

### 5. End with approval gate
- Ask whether to proceed to `/plan-verify`

Do not start implementation from this skill. Planning only.

$ARGUMENTS
