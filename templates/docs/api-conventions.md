# API Conventions

API design patterns and conventions for {{PROJECT_NAME}}.

<!-- NOTE: This file covers conventions and patterns only. Do not duplicate full API
     reference documentation here. If the project has existing API docs (e.g., Swagger,
     OpenAPI, Redoc), link to them below instead.
-->

{{API_DOCS_LINK}}

<!-- Examples:
  - Full API reference: see `docs/openapi.yaml`
  - Swagger UI available at http://localhost:3000/api-docs when running dev server
  - API docs generated from source: run `npm run docs:api`
-->

## Endpoint Patterns

{{ENDPOINT_PATTERNS}}

<!-- Describe the API structure:
  - URL naming conventions (REST, RPC-style, etc.)
  - HTTP method usage
  - Versioning strategy
  - Example endpoints
-->

## Request/Response Format

{{REQUEST_RESPONSE_FORMAT}}

<!-- Describe the standard format:
  - Content type (JSON, XML, etc.)
  - Envelope format (if any)
  - Pagination approach
  - Field naming convention (camelCase, snake_case)
-->

## Error Handling

{{ERROR_HANDLING}}

<!-- Describe error conventions:
  - Error response format
  - Error codes and their meanings
  - How errors propagate through the system
  - Logging and monitoring
-->

## Authentication & Authorization

{{AUTH_PATTERNS}}

<!-- Describe auth patterns:
  - Authentication mechanism (JWT, session, API key)
  - Authorization model (RBAC, ABAC, etc.)
  - How to add auth to new endpoints
-->

## Adding New Endpoints

{{NEW_ENDPOINT_GUIDE}}

<!-- Step-by-step guide for adding a new endpoint:
  1. Define the route
  2. Add validation
  3. Implement handler
  4. Add tests
  5. Update API docs
-->

## Related Docs

- @docs/architecture.md — System architecture
- @docs/testing.md — How to test API endpoints
