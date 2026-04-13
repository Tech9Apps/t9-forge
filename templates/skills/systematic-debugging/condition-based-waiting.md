# Condition-Based Waiting

## Overview

Flaky tests often guess at timing with arbitrary delays. This creates race conditions where tests pass on fast machines but fail under load or in CI.

**Core principle:** Wait for the actual condition you care about, not a guess about how long it takes.

## When to Use

- Tests have arbitrary delays (`setTimeout`, `sleep`, `time.sleep()`)
- Tests are flaky (pass sometimes, fail under load)
- Tests timeout when run in parallel
- Waiting for async operations to complete

**Don't use when** testing actual timing behavior (debounce, throttle intervals). Always document WHY if using an arbitrary timeout.

## Core Pattern

```
// BAD: Guessing at timing
await sleep(50);
const result = getResult();
assert(result !== undefined);

// GOOD: Waiting for condition
await waitFor(() => getResult() !== undefined);
const result = getResult();
assert(result !== undefined);
```

## Quick Patterns

| Scenario | Pattern |
|----------|---------|
| Wait for event | `waitFor(() => events.find(e => e.type === 'DONE'))` |
| Wait for state | `waitFor(() => machine.state === 'ready')` |
| Wait for count | `waitFor(() => items.length >= 5)` |
| Wait for file | `waitFor(() => fileExists(path))` |
| Complex condition | `waitFor(() => obj.ready && obj.value > 10)` |

## Implementation

Generic polling function (adapt to your language):

```
function waitFor(condition, description, timeoutMs = 5000):
  startTime = now()
  while true:
    result = condition()
    if result: return result
    if now() - startTime > timeoutMs:
      throw Error("Timeout waiting for {description} after {timeoutMs}ms")
    sleep(10ms)  // Poll every 10ms
```

<!-- Examples for common stacks:
  Node/TypeScript: Use async/await with setTimeout in a while loop
  Python: Use time.time() and time.sleep(0.01) in a while loop
  Rust: Use tokio::time::sleep and Instant::now()
  Go: Use time.NewTicker and time.After with select
-->

## Common Mistakes

- **Polling too fast:** `sleep(1ms)` wastes CPU. Poll every 10ms.
- **No timeout:** Loop forever if condition never met. Always include a timeout with a clear error.
- **Stale data:** Caching state before the loop. Call the getter inside the loop for fresh data.

## When Arbitrary Timeout IS Correct

When testing actual timed behavior:

1. First wait for the triggering condition (use condition-based waiting)
2. Then wait for the timed behavior (arbitrary delay)
3. Document WHY the specific duration was chosen

```
// Tool ticks every 100ms — need 2 ticks to verify partial output
await waitForEvent(manager, 'TOOL_STARTED');  // First: condition
await sleep(200);  // Then: 2 ticks at 100ms intervals (documented)
```
