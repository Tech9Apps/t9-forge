# /writing-plans

Write comprehensive implementation plans with bite-sized tasks, exact code, and no placeholders.

## Instructions

### Overview

Write implementation plans assuming the engineer has zero context for the codebase. Document everything they need: which files to touch for each task, complete code, how to test it. Give them the whole plan as bite-sized tasks. DRY. YAGNI. TDD. Frequent commits.

Assume they are a skilled developer, but know almost nothing about the toolset or problem domain. Assume they don't know good test design very well.

### 1. Scope Check

If the spec covers multiple independent subsystems, suggest breaking this into separate plans — one per subsystem. Each plan should produce working, testable software on its own.

### 2. Map File Structure

Before defining tasks, map out which files will be created or modified and what each one is responsible for. This is where decomposition decisions get locked in.

- Design units with clear boundaries and well-defined interfaces
- Prefer smaller, focused files over large ones that do too much
- Files that change together should live together. Split by responsibility, not by technical layer.
- In existing codebases, follow established patterns

This structure informs the task decomposition. Each task should produce self-contained changes that make sense independently.

### 3. Write Tasks with Bite-Sized Granularity

**Each step is one action (2–5 minutes):**
- "Write the failing test" — step
- "Run it to make sure it fails" — step
- "Implement the minimal code to make the test pass" — step
- "Run the tests and make sure they pass" — step
- "Commit" — step

### 4. Plan Document Header

Every plan MUST start with this header:

```markdown
# [Feature Name] Implementation Plan

**Goal:** [One sentence describing what this builds]

**Architecture:** [2-3 sentences about approach]

**Tech Stack:** [Key technologies/libraries]

---
```

### 5. Task Structure

Each task follows this format:

````markdown
### Task N: [Component Name]

**Files:**
- Create: `exact/path/to/file`
- Modify: `exact/path/to/existing:123-145`
- Test: `exact/path/to/test`

- [ ] **Step 1: Write the failing test**

```
(actual test code here)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `{{TEST_COMMAND}} path/to/test`
Expected: FAIL with "function not defined"

- [ ] **Step 3: Write minimal implementation**

```
(actual implementation code here)
```

- [ ] **Step 4: Run test to verify it passes**

Run: `{{TEST_COMMAND}} path/to/test`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add <files>
git commit -m "feat: add specific feature"
```
````

<!-- Examples for test commands:
  Node/TypeScript: npx jest path/to/test.test.ts -v
  Python: pytest tests/path/test.py::test_name -v
  Rust: cargo test test_name
  Go: go test ./path/... -run TestName -v
-->

### 6. No Placeholders

Every step must contain the actual content an engineer needs. These are **plan failures** — never write them:

- "TBD", "TODO", "implement later", "fill in details"
- "Add appropriate error handling" / "add validation" / "handle edge cases"
- "Write tests for the above" (without actual test code)
- "Similar to Task N" (repeat the code — the engineer may read tasks out of order)
- Steps that describe what to do without showing how (code blocks required for code steps)
- References to types, functions, or methods not defined in any task

### 7. Self-Review

After writing the complete plan, check it against the spec:

1. **Spec coverage:** Skim each section/requirement in the spec. Can you point to a task that implements it? List any gaps.
2. **Placeholder scan:** Search your plan for red flags — any of the patterns from the "No Placeholders" section. Fix them.
3. **Type consistency:** Do the types, method signatures, and property names used in later tasks match what you defined in earlier tasks?

If you find issues, fix them inline. If you find a spec requirement with no task, add the task.

### 8. Save the Plan

Save to:

```
{{PLAN_LOCATION}}/YYYY-MM-DD-<feature-name>.md
```

<!-- Examples for plan locations:
  Default: docs/plans/
  Alternative: docs/implementation-plans/
  Alternative: plans/
-->

### 9. Execution Handoff

After saving the plan, offer the execution choice:

> "Plan complete and saved to `<path>`. Two execution options:
>
> 1. **Subagent-Driven (recommended)** — Consider using `/subagent-dev` to dispatch a fresh subagent per task with two-stage review
> 2. **Inline Execution** — Execute tasks in this session, batch execution with checkpoints
>
> Which approach?"

### Key Rules

- Exact file paths always
- Complete code in every step — if a step changes code, show the code
- Exact commands with expected output
- DRY, YAGNI, TDD, frequent commits
- Use `{{BUILD_COMMAND}}` and `{{VERIFY_COMMAND}}` for final verification steps

### Plan Review (Subagent)

For larger plans, dispatch a plan reviewer subagent using the template in @plan-reviewer-prompt.md to verify the plan is complete, matches the spec, and has proper task decomposition.
