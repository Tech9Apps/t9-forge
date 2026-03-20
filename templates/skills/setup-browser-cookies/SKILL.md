# /setup-browser-cookies

Import browser session cookies for authenticated QA/browse flows.

## Instructions

### 1. Capability gate
- Requires secure cookie import support on current platform/runtime.
- If unsupported, provide fallback guidance (manual login flow for QA sessions).

### 2. Import scope
- Prefer explicit domain arguments when provided.
- Otherwise offer interactive domain selection.

### 3. Security posture
- Never print cookie values.
- Report only domain-level import counts and status.

### 4. Output
- Imported domains and cookie counts.
- Session readiness for `/browse` and `/qa`.
- Any platform limitations detected.

$ARGUMENTS
