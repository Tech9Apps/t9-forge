---
description: "Run relevant tests based on currently changed files. Use when the user wants to test their changes, run tests, or verify a change before committing."
user-invocable: true
argument-hint: "[file|directory|pattern]"
---

# /test

Run relevant tests based on current changes.

## Instructions

### 1. Identify Changed Files

Run `git diff --name-only` and `git diff --staged --name-only` to find modified files.

### 2. Find Related Tests

For each changed file, locate associated test files:

{{TEST_FILE_PATTERNS}}

<!-- Examples for common stacks:
  Node/TypeScript: src/foo.ts → src/foo.test.ts, src/__tests__/foo.test.ts, test/foo.test.ts
  Python: src/foo.py → tests/test_foo.py, src/foo_test.py, tests/foo/test_foo.py
  Rust: src/foo.rs → tests in the same file (#[cfg(test)]) or tests/foo.rs
  Go: pkg/foo.go → pkg/foo_test.go
-->

### 3. Run Tests

Run the identified tests using the project's test runner:

```
{{TEST_COMMAND}}
```

<!-- Examples for common stacks:
  Node/TypeScript: npx jest --findRelatedTests <files>
  Python: pytest <test_files>
  Rust: cargo test <test_name>
  Go: go test ./<package>/...
-->

If no specific tests are found for the changed files, ask the user whether to:
- Run the full test suite: `{{TEST_ALL_COMMAND}}`
- Skip testing

### 4. Report Results

Summarize test results:
- Number of tests run, passed, failed
- Details on any failures
- Suggestions for fixing failures if applicable

$ARGUMENTS

If arguments are provided, use them to scope the test run (e.g., a specific file, directory, or test name pattern).
