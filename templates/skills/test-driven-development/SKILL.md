# /test-driven-development

Write the test first. Watch it fail. Write minimal code to pass. No exceptions.

## Instructions

### Iron Law

```
NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST
```

Write code before the test? Delete it. Start over.

**No exceptions:**
- Don't keep it as "reference"
- Don't "adapt" it while writing tests
- Don't look at it
- Delete means delete

Implement fresh from tests. Period.

**Core principle:** If you didn't watch the test fail, you don't know if it tests the right thing.

Violating the letter of the rules is violating the spirit of the rules.

### When to Use

**Always:**
- New features
- Bug fixes
- Refactoring
- Behavior changes

**Exceptions (ask the user):**
- Throwaway prototypes
- Generated code
- Configuration files

Thinking "skip TDD just this once"? Stop. That's rationalization.

### 1. RED — Write Failing Test

Write one minimal test showing what should happen.

**Good:**
```
// Clear name, tests real behavior, one thing
test('retries failed operations 3 times', () => {
  let attempts = 0;
  const operation = () => {
    attempts++;
    if (attempts < 3) throw new Error('fail');
    return 'success';
  };
  const result = retryOperation(operation);
  assert(result === 'success');
  assert(attempts === 3);
});
```

<!-- Examples for common stacks:
  Node/TypeScript: Use jest/vitest with expect()
  Python: Use pytest with assert
  Rust: Use #[test] with assert_eq!
  Go: Use testing.T with t.Fatal/t.Error
-->

**Bad:**
```
// Vague name, tests mock not code
test('retry works', () => {
  const mock = createMock()
    .failTwice()
    .thenSucceed();
  retryOperation(mock);
  assert(mock.callCount === 3);
});
```

**Requirements:**
- One behavior per test
- Clear name describing the behavior
- Real code (no mocks unless unavoidable)

### 2. Verify RED — Watch It Fail

**MANDATORY. Never skip.**

```
{{TEST_COMMAND}}
```

Confirm:
- Test fails (not errors)
- Failure message is expected
- Fails because feature missing (not typos)

**Test passes?** You're testing existing behavior. Fix the test.

**Test errors?** Fix the error, re-run until it fails correctly.

### 3. GREEN — Minimal Code

Write the simplest code to pass the test.

**Good:** Just enough to pass — no more.

**Bad:** Over-engineered with options, callbacks, and configurability nobody asked for (YAGNI).

Don't add features, refactor other code, or "improve" beyond the test.

### 4. Verify GREEN — Watch It Pass

**MANDATORY.**

```
{{TEST_COMMAND}}
```

Confirm:
- Test passes
- Other tests still pass
- Output pristine (no errors, warnings)

**Test fails?** Fix code, not test.

**Other tests fail?** Fix now.

### 5. REFACTOR — Clean Up

After green only:
- Remove duplication
- Improve names
- Extract helpers

Keep tests green. Don't add behavior.

Then run:

```
{{TEST_ALL_COMMAND}}
```

### 6. Repeat

Next failing test for next behavior.

### Good Tests

| Quality | Good | Bad |
|---------|------|-----|
| **Minimal** | One thing. "and" in name? Split it. | `test('validates email and domain and whitespace')` |
| **Clear** | Name describes behavior | `test('test1')` |
| **Shows intent** | Demonstrates desired API | Obscures what code should do |

### Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "Too simple to test" | Simple code breaks. Test takes 30 seconds. |
| "I'll test after" | Tests passing immediately prove nothing. |
| "Tests after achieve same goals" | Tests-after = "what does this do?" Tests-first = "what should this do?" |
| "Already manually tested" | Ad-hoc ≠ systematic. No record, can't re-run. |
| "Deleting X hours is wasteful" | Sunk cost fallacy. Keeping unverified code is technical debt. |
| "Keep as reference, write tests first" | You'll adapt it. That's testing after. Delete means delete. |
| "Need to explore first" | Fine. Throw away exploration, start with TDD. |
| "Test hard = design unclear" | Listen to the test. Hard to test = hard to use. |
| "TDD will slow me down" | TDD faster than debugging. |
| "Manual test faster" | Manual doesn't prove edge cases. You'll re-test every change. |
| "Existing code has no tests" | You're improving it. Add tests for existing code. |

### Red Flags — STOP and Start Over

- Code before test
- Test after implementation
- Test passes immediately
- Can't explain why test failed
- Tests added "later"
- Rationalizing "just this once"
- "Keep as reference" or "adapt existing code"
- "Already spent X hours, deleting is wasteful"
- "This is different because..."

**All of these mean: Delete code. Start over with TDD.**

### Bug Fix Workflow

1. **RED:** Write a test that reproduces the bug
2. **Verify RED:** Confirm the test fails
3. **GREEN:** Fix the bug with minimal code
4. **Verify GREEN:** Confirm the test passes
5. **REFACTOR:** Extract validation if needed

Never fix bugs without a test.

### When Stuck

| Problem | Solution |
|---------|----------|
| Don't know how to test | Write wished-for API. Write assertion first. Ask the user. |
| Test too complicated | Design too complicated. Simplify interface. |
| Must mock everything | Code too coupled. Use dependency injection. |
| Test setup huge | Extract helpers. Still complex? Simplify design. |

### Testing Anti-Patterns

When adding mocks or test utilities, read @testing-anti-patterns.md to avoid common pitfalls:
- Testing mock behavior instead of real behavior
- Adding test-only methods to production classes
- Mocking without understanding dependencies

### Verification Checklist

Before marking work complete:

- [ ] Every new function/method has a test
- [ ] Watched each test fail before implementing
- [ ] Each test failed for expected reason (feature missing, not typo)
- [ ] Wrote minimal code to pass each test
- [ ] All tests pass
- [ ] Output pristine (no errors, warnings)
- [ ] Tests use real code (mocks only if unavoidable)
- [ ] Edge cases and errors covered

Can't check all boxes? You skipped TDD. Start over.

### Final Rule

```
Production code → test exists and failed first
Otherwise → not TDD
```

No exceptions without the user's permission.
