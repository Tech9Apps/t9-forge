# /systematic-debugging

Systematic root-cause debugging process — investigate before fixing, verify before claiming.

## Instructions

### Iron Law

```
NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST
```

**Core principle:** ALWAYS find root cause before attempting fixes. Symptom fixes are failure.

### 1. Root Cause Investigation

Before attempting any fix:

1. **Read error messages completely** — the answer is often in the output
2. **Reproduce the issue consistently** — if you can't reproduce it, you can't verify a fix
3. **Check recent changes** — what changed between "working" and "broken"?
4. **Gather diagnostic evidence** — logs, stack traces, state at time of failure
5. **Trace data flow backward** — follow the call chain from symptom to source

```
{{TEST_COMMAND}}
```

<!-- Examples for common stacks:
  Node/TypeScript: npx jest --findRelatedTests <files>
  Python: pytest <test_files> -v
  Rust: cargo test <test_name>
  Go: go test ./<package>/... -v
-->

For detailed tracing techniques, see @root-cause-tracing.md

### 2. Pattern Analysis

Once you have diagnostic evidence:

1. **Locate working examples** — find similar code that works correctly
2. **Read reference implementations thoroughly** — don't skim
3. **Identify differences** between working and broken code
4. **Understand all dependencies** — the bug may be in a dependency, not your code

### 3. Hypothesis and Testing

Apply scientific methodology:

1. **Form a specific hypothesis** — "The bug is caused by X because Y"
2. **Make minimal testable changes** — one variable at a time
3. **Verify the hypothesis** — does the change fix the symptom?
4. **Never apply multiple simultaneous fixes** — you won't know which one worked

### 4. Implementation

Once root cause is confirmed:

1. **Create a failing test case first** — proves the bug exists and prevents regression
2. **Implement a single targeted fix** — address the root cause, not the symptom
3. **Verify results** — run the full verification chain

```
{{VERIFY_COMMAND}}
```

For defense-in-depth validation strategies, see @defense-in-depth.md

For replacing arbitrary timeouts with condition-based waiting, see @condition-based-waiting.md

### 5. The Three-Strike Rule

```
IF 3+ FIXES FAILED: QUESTION THE ARCHITECTURE
```

When multiple attempted fixes each reveal new problems in different locations, this signals an architectural issue — not a series of independent bugs.

**Stop patching. Reassess:**
- Is the component trying to do too much?
- Are responsibilities in the wrong place?
- Is there a fundamental design mismatch?

Discuss with the user before continuing. More patches will not fix a structural problem.

### Red Flags — STOP

- Proposing a solution before investigating
- Saying "just try this" without a hypothesis
- Attempting "just one more fix" after multiple failures
- Fixing where the error appears instead of where it originates
- Assuming you understand the problem without verification
- Skipping reproduction ("I think I know what's wrong")
- Applying multiple changes at once

### Why This Matters

Systematic debugging is actually faster than guess-and-check, particularly under time pressure when shortcuts seem most tempting. Each failed guess wastes more time than methodical investigation would have taken.

**Under pressure:**
- Shortcuts feel faster but compound the problem
- Each wrong fix introduces new variables
- Methodical investigation converges; guessing diverges
