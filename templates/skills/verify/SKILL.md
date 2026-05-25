---
description: "Run the full verification chain (build, lint, type-check, tests) to confirm the project is healthy. Use before declaring work complete, before opening a PR, or when the user asks to verify everything passes."
user-invocable: true
---

# /verify

Run the full verification chain to confirm the project is in a healthy state.

## Instructions

Run each of the following steps in order. Stop and report if any step fails.

### 1. Build

```
{{BUILD_COMMAND}}
```

<!-- Examples for common stacks:
  Node/TypeScript: npm run build
  Python: python -m py_compile src/**/*.py
  Rust: cargo build
  Go: go build ./...
-->

If there is no build step for this project, skip this.

### 2. Lint

```
{{LINT_COMMAND}}
```

<!-- Examples for common stacks:
  Node/TypeScript: npx eslint .
  Python: ruff check .
  Rust: cargo clippy
  Go: golangci-lint run
-->

### 3. Type Check

```
{{TYPECHECK_COMMAND}}
```

<!-- Examples for common stacks:
  Node/TypeScript: npx tsc --noEmit
  Python: mypy src/
  Rust: (covered by cargo build)
  Go: (covered by go build)
-->

If there is no separate type-check step, skip this.

### 4. Tests

```
{{TEST_ALL_COMMAND}}
```

<!-- Examples for common stacks:
  Node/TypeScript: npm test
  Python: pytest
  Rust: cargo test
  Go: go test ./...
-->

### 5. Report

Summarize results:
- Which steps passed
- Which steps failed (with relevant error output)
- Suggested fixes for any failures
