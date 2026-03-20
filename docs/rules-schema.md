# Canonical Rules Schema

The toolkit builds one normalized rules object, then renders it to Claude and Cursor outputs.

Schema location: `config/rules-schema.json`

## Required fields

- `schemaVersion`
- `projectProfile`
- `architectureRules`
- `apiRules`
- `testingRules`
- `workflowRules`
- `securityRules`

All generators should treat these fields as required contract inputs.

## Renderer mapping

- Claude renderer:
  - `CLAUDE.md` sections
- Cursor renderer:
  - `AGENTS.md`
  - `.cursor/rules/architecture.mdc`
  - `.cursor/rules/api-and-data.mdc`
  - `.cursor/rules/testing.mdc`
  - `.cursor/rules/workflow.mdc`

If a target does not support a surface (for example hooks on Cursor), do not synthesize fake equivalents.

## Capability model

The canonical model now supports two capability dimensions:

- `projectProfile.runtimeCapabilities`
  - discovered runtime/tooling facts from repository + environment
  - keys:
    - `hasGitRepo`
    - `hasGitHubCli`
    - `hasBun`
    - `hasBrowserAutomationBackend`
    - `supportsMacOSKeychainImport`

- `workflowRules.workflowCapabilities`
  - per-workflow classification:
    - `portable` for prompt-only workflows
    - `runtime-backed` for workflows that depend on local runtime/tooling
  - workflow keys:
    - `planCeoReview`
    - `planEngReview`
    - `planDesignReview`
    - `review`
    - `ship`
    - `browse`
    - `qa`
    - `qaOnly`
    - `qaDesignReview`
    - `setupBrowserCookies`
    - `retro`
    - `documentRelease`

Optional `workflowRules.fallbackPolicy` defines behavior when a required capability is missing:

- `skip`
- `report-only`
- `ask-user`

## Target capability mapping

Target config files in `config/targets/*.json` include renderer support flags:

- `supportsHooks`
- `supportsBrowserAutomation`
- `supportsCookieImport`
- `supportsGitHubPR`
- `supportsRetrospectives`
- `supportsRuntimeArtifacts`

Renderers should intersect target flags with discovered runtime capabilities before including runtime-backed behavior. Example:

- Cursor may support browser automation but skip cookie import if unavailable.
- Claude can generate runtime artifacts under `.claude/*`; Cursor should keep runtime behavior in rule guidance only.

## Versioning rule

If schema changes are backward-incompatible:
- bump `schemaVersion`
- update tests in `tests/test_contracts.py`
- update templates consuming affected fields

For non-breaking changes, keep field compatibility and extend tests.
