# Root Cause Tracing

## Overview

Bugs often manifest deep in the call stack. Your instinct is to fix where the error appears, but that's treating a symptom.

**Core principle:** Trace backward through the call chain until you find the original trigger, then fix at the source.

## When to Use

- Error happens deep in execution (not at entry point)
- Stack trace shows long call chain
- Unclear where invalid data originated
- Need to find which test/code triggers the problem

## The Tracing Process

### 1. Observe the Symptom

Note the exact error message and location.

### 2. Find Immediate Cause

What code directly produces this error?

### 3. Ask: What Called This?

Trace one level up. What function called this one, and with what arguments?

### 4. Keep Tracing Up

Follow the chain. At each level, check: is the data already wrong here, or does it become wrong at this level?

### 5. Find Original Trigger

The root cause is the earliest point in the chain where the data becomes invalid.

**Example trace (5 levels):**

```
Error: operation failed in unexpected directory
  → function called with empty string as `cwd`
    → caller passed value from uninitialized variable
      → variable accessed before setup completed
        → test accessed context before beforeEach ran
          → ROOT CAUSE: top-level variable initialization
```

## Adding Stack Traces

When you can't trace manually, add instrumentation:

```
// Before the problematic operation, log:
// - The input values
// - The current working directory or environment
// - The full stack trace (new Error().stack or equivalent)
// - Any relevant environment variables
```

<!-- Examples for common stacks:
  Node/TypeScript: console.error('DEBUG:', { directory, cwd: process.cwd(), stack: new Error().stack })
  Python: import traceback; print(f"DEBUG: {vars()}", traceback.format_stack())
  Rust: eprintln!("DEBUG: {:?}", std::backtrace::Backtrace::capture())
  Go: debug.PrintStack()
-->

**Tips:**
- Use stderr for debug output in tests (stdout may be suppressed)
- Log **before** the dangerous operation, not after it fails
- Include context: directory, environment variables, timestamps
- Capture the full stack trace to show the complete call chain

## Finding Which Test Causes Pollution

If something appears during tests but you don't know which test:

1. Run tests individually to isolate the polluter
2. Use binary search: run first half, then second half
3. Once narrowed down, run the suspect test alone to confirm

## Key Principle

**NEVER fix just where the error appears.** Trace back to find the original trigger. Then add validation at each layer the data passes through (see @defense-in-depth.md).
