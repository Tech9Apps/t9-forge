# Testing Anti-Patterns

**Load this reference when:** writing or changing tests, adding mocks, or tempted to add test-only methods to production code.

## Overview

Tests must verify real behavior, not mock behavior. Mocks are a means to isolate, not the thing being tested.

**Core principle:** Test what the code does, not what the mocks do.

**Following strict TDD prevents these anti-patterns.**

## The Iron Laws

```
1. NEVER test mock behavior
2. NEVER add test-only methods to production classes
3. NEVER mock without understanding dependencies
```

## Anti-Pattern 1: Testing Mock Behavior

**The violation:**
```
// BAD: Testing that the mock exists
test('renders sidebar', () => {
  render(Page);
  expect(screen.getByTestId('sidebar-mock')).toBeInTheDocument();
});
```

**Why this is wrong:**
- You're verifying the mock works, not that the component works
- Test passes when mock is present, fails when it's not
- Tells you nothing about real behavior

**The fix:**
```
// GOOD: Test real component or don't mock it
test('renders sidebar', () => {
  render(Page);  // Don't mock sidebar
  expect(screen.getByRole('navigation')).toBeInTheDocument();
});
```

**Gate:** Before asserting on any mock element, ask: "Am I testing real behavior or just mock existence?" If testing mock existence — delete the assertion or unmock the component.

## Anti-Pattern 2: Test-Only Methods in Production

**The violation:** Adding a `destroy()` or `reset()` method to a production class that is only ever called from tests.

**Why this is wrong:**
- Production class polluted with test-only code
- Dangerous if accidentally called in production
- Violates YAGNI and separation of concerns

**The fix:** Move cleanup logic to test utilities.

```
// BAD: destroy() only used in tests
class Session {
  destroy() { /* cleanup */ }
}

// GOOD: Test utilities handle test cleanup
// test-utils/
function cleanupSession(session) {
  // cleanup logic lives here, not in production code
}
```

**Gate:** Before adding any method to a production class, ask: "Is this only used by tests?" If yes — put it in test utilities instead.

## Anti-Pattern 3: Mocking Without Understanding

**The violation:** Mocking a method that has side effects your test depends on.

**Why this is wrong:**
- Mocked method had a side effect the test needed (e.g., writing config)
- Over-mocking to "be safe" breaks actual behavior
- Test passes for the wrong reason or fails mysteriously

**The fix:** Mock at the correct level. Mock the slow part (network, filesystem), preserve the behavior your test needs.

**Gate:** Before mocking any method:
1. Ask: "What side effects does the real method have?"
2. Ask: "Does this test depend on any of those side effects?"
3. If yes — mock at a lower level, not the high-level method the test depends on

Red flags: "I'll mock this to be safe" or "This might be slow, better mock it" without understanding the dependency chain.

## Anti-Pattern 4: Incomplete Mocks

**The violation:** Creating a mock with only the fields you think you need, missing fields that downstream code uses.

**Why this is wrong:**
- Partial mocks hide structural assumptions
- Downstream code may depend on fields you didn't include
- Tests pass but integration fails — false confidence

**The fix:** Mirror the real data structure completely. If you're creating a mock, you must understand the ENTIRE structure.

**Gate:** Before creating mock responses, check: "What fields does the real response contain?" Include ALL fields the system might consume downstream.

## Anti-Pattern 5: Integration Tests as Afterthought

**The violation:** Claiming implementation is complete without tests.

**The fix:** Testing is part of implementation, not an optional follow-up. TDD prevents this by construction.

## Quick Reference

| Anti-Pattern | Fix |
|--------------|-----|
| Assert on mock elements | Test real component or unmock it |
| Test-only methods in production | Move to test utilities |
| Mock without understanding | Understand dependencies first, mock minimally |
| Incomplete mocks | Mirror real API completely |
| Tests as afterthought | TDD — tests first |
| Over-complex mocks | Consider integration tests |

## Red Flags

- Assertion checks for `*-mock` test IDs
- Methods only called in test files
- Mock setup is >50% of test
- Test fails when you remove mock
- Can't explain why mock is needed
- Mocking "just to be safe"

## The Bottom Line

**Mocks are tools to isolate, not things to test.**

If you find yourself testing mock behavior, you've gone wrong. Test real behavior or question why you're mocking at all.
