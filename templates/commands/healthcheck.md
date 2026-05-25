---
description: "Project health dashboard: git status, branch state, recent commits, and a quick view of project health."
---

# Project Status

Show the current state of the project.

## Instructions

Run the following and present a summary:

### Git Status
```bash
git status --short --branch
git log --oneline -5
```

### Build Health
```bash
{{BUILD_COMMAND}}
```

<!-- Examples:
  Node: npm run build
  Python: python -m py_compile <main_module>
  Rust: cargo check
  Go: go build ./...
-->

### Test Status
```bash
{{TEST_ALL_COMMAND}}
```

### Lint Status
```bash
{{LINT_COMMAND}}
```

Present results as a concise dashboard:
- Branch and recent commits
- Build status (pass/fail)
- Test results (pass/fail count)
- Lint issues (count)

$ARGUMENTS
