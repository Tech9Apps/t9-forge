# /plan-verify

Critically verify a proposed plan before execution.

## Instructions

Treat this as a mandatory quality gate before implementation.

### 1. Validate completeness
- Does the plan include all affected components?
- Are migrations/config changes covered?
- Are edge cases explicitly handled?

### 2. Validate correctness
- Identify missing dependencies
- Identify ordering hazards
- Identify unsafe assumptions

### 3. Validate verification coverage
- Ensure test/lint/build/typecheck steps are present where applicable
- Ensure deploy/rollback checks are present for release-impacting work

### 4. Report with strict structure
- Number issues (`Issue 1`, `Issue 2`, ...)
- For each issue provide option letters (`A`, `B`, `C`)
- Put recommended option first
- Include effort, risk, impact, maintenance burden
- Ask for explicit user choice before patching the plan

### 5. If no issues
- Explicitly state the plan is execution-ready

Do not execute implementation tasks from this skill.

$ARGUMENTS
