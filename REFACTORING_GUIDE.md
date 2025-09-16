# Refactoring Guide (for reviewers)

This describes issues a candidate can reasonably find and fix in 10–15 minutes. Do not include this with candidate instructions until after the exercise.

## Backend (FastAPI)
- Hardcoded credentials and token in `backend/main.py`.
  - Extract to environment variables/config; never commit secrets.
- Inconsistent auth: `/dog` has no auth; others do.
  - Standardize with a FastAPI dependency (e.g., `Depends(auth)`), and protect only what should be protected.
- Token handling scattered and weak: reads from query or header.
  - Use `Authorization: Bearer <token>` only. Remove query token and duplicated checks.
- Blocking HTTP calls with `requests` in sync endpoints.
  - Convert to `async def` and use `httpx.AsyncClient`.
- Mixed concerns: routes fetch and transform external data and mutate global state.
  - Move fetching/transformations to a small service module; keep handlers thin.
- Global mutable `STATE` used as cache/auth storage.
  - Remove or replace with request-scoped data or a simple in-memory cache with TTL.
- Overly broad CORS (`*`).
  - Restrict to dev origin or make it configurable.
- Error handling leaks details and swallows exceptions.
  - Return generic messages to clients; log details server-side.

## Frontend (Vue)
- Everything in `frontend/src/main.js` (logic, view, API calls).
  - Split into components (Login, Users, Dog, Secret) and extract an `api.js` module.
- Hardcoded backend URL and token fallback.
  - Move to `.env` via `VITE_API_URL` and remove default token.
- Confusing dual auth path (header + query param).
  - Use only the `Authorization` header.
- Minimal error handling and state sharing.
  - Add simple reactive state or props/emit with clear error UI.
- Unused Vite proxy config.
  - Either adopt `/api` base path or remove the proxy.

## Quick-win checklist
- Backend: add `auth.py` dependency, switch to async + `httpx`, narrow CORS, remove globals.
- Frontend: add `api.js`, env-based baseURL, split components, consistent auth header, remove query token.

## Optional stretch
- Pydantic models for request/response validation.
- Basic tests for service functions.
- Simple retry/timeout policy for external APIs.
