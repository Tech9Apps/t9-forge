---
description: "Read library documentation before using it: fetches docs, checks latest version, verifies compatibility. Use when adding a new dependency or working with an unfamiliar library."
user-invocable: true
argument-hint: "<library-name>"
---

# /use-library

Read library documentation before using it. Fetches docs, checks latest version, verifies compatibility.

Do NOT write implementation code until documentation has been read.

## Instructions

$ARGUMENTS is required — provide the library/package name.

### 1. Detect Stack and Check if Already Installed

Check if the library is already in the project:

```
{{DEPENDENCY_FILE}}
```

<!-- Examples for dependency files:
  Node/TypeScript: package.json
  Python: pyproject.toml, requirements.txt
  Ruby: Gemfile
  Go: go.mod
  Elixir: mix.exs
  Rust: Cargo.toml
-->

If already present, note the current version and check if an upgrade is needed.

### 2. Get Library Info

Look up the library in the package registry:

```
{{PACKAGE_INFO_COMMAND}}
```

<!-- Examples for common stacks:
  Node/TypeScript: npm view $ARGUMENTS version description homepage
  Python: pip show $ARGUMENTS
  Ruby: gem specification $ARGUMENTS
  Go: go doc $ARGUMENTS
  Elixir: mix hex.info $ARGUMENTS
  Rust: cargo search $ARGUMENTS
-->

### 3. Read Documentation

Fetch the library's official documentation or README:
- If a homepage URL was found, fetch it
- Otherwise search for the library's documentation or GitHub README
- Read at minimum: installation instructions, basic usage, API reference for needed features

### 4. Check Latest Version

Verify you're recommending the LATEST stable version:

```
{{PACKAGE_VERSION_COMMAND}}
```

<!-- Examples for common stacks:
  Node/TypeScript: npm view $ARGUMENTS version
  Python: pip index versions $ARGUMENTS
  Ruby: gem search -r $ARGUMENTS
  Go: go list -m -versions $ARGUMENTS
  Elixir: mix hex.info $ARGUMENTS
  Rust: cargo search $ARGUMENTS
-->

If the project already uses this library at a different version, check the changelog for breaking changes.

### 5. Install and Verify

1. Add the dependency with appropriate version constraint
2. Install:

```
{{INSTALL_COMMAND}}
```

<!-- Examples for common stacks:
  Node/TypeScript: npm install
  Python: pip install -r requirements.txt
  Ruby: bundle install
  Go: go mod tidy
  Elixir: mix deps.get
  Rust: cargo build
-->

3. Run the test suite: `{{TEST_ALL_COMMAND}}`
4. Run security audit: `{{SECURITY_AUDIT_COMMAND}}`

$ARGUMENTS
