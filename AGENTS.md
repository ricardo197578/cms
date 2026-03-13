# AGENTS.md - Editorial CMS

Guide for coding agents operating in this repository.

## Project Snapshot

- Stack: Python 3.x, Reflex `0.8.27`, SQLModel, PostgreSQL, Alembic, bcrypt.
- App package: `editorial_cms/`.
- Domain language in code/UI is mostly Spanish (`Usuario`, `titulo`, `categoria`, etc.).
- Architecture pattern: models -> services -> states -> pages/components.
- Database URL is loaded from `.env` via `DATABASE_URL`.

## Build, Run, Lint, Test

Use the project virtualenv when available (`venv`).

```bash
# Install runtime dependencies
pip install -r requirements.txt

# Run app (dev)
reflex run

# Run app on custom port
reflex run --port 3000

# Production deploy build
reflex deploy

# Lint (ruff is not pinned in requirements)
pip install ruff
ruff check .
ruff check --fix .

# Optional format pass (if adopted in PR)
ruff format .

# Tests (currently no tests folder in repo)
pip install pytest pytest-asyncio
pytest

# Run a single test file
pytest tests/test_post_service.py

# Run a single test function
pytest tests/test_post_service.py::test_crear_post

# Run tests by keyword expression
pytest -k "post and crear"
```

## Database and Migrations

```bash
# Apply migrations (if migration env is configured)
alembic upgrade head

# Create migration draft
alembic revision --autogenerate -m "descripcion"
```

Notes:
- `init_db()` is called at app startup (`editorial_cms/editorial_cms.py`).
- `editorial_cms/database.py` loads `.env` with `dotenv` and builds the SQLModel engine.

## Code Style Guidelines

### Language and Naming

- Keep business/domain naming in Spanish unless extending an already-English module.
- Files/modules: `snake_case`.
- Classes: `PascalCase`.
- Functions/methods/variables: `snake_case`.
- State classes must end with `State`.
- Service names should use CRUD verbs: `crear_*`, `obtener_*`, `actualizar_*`, `eliminar_*`.

### Imports

- Prefer absolute imports from `editorial_cms.*`.
- Group imports: stdlib, third-party, local (one blank line between groups).
- Avoid duplicate imports within the same file.
- Avoid inline imports unless needed to break circular dependencies.

### Typing

- Add type hints on public function parameters and return values.
- Use `Optional[T]`/`T | None` consistently for nullable data.
- SQLModel models should type all fields explicitly.
- Reflex state attributes should be typed (`str`, `int`, `list[Post]`, etc.).

### Formatting and Structure

- Follow PEP 8 and keep functions cohesive.
- Prefer small service functions with one responsibility.
- Move reusable logic (slugging, filtering, auth checks) into service/helper functions.
- Avoid dead commented blocks unless they are temporary and justified in PR context.

### Error Handling

- Never expose raw exceptions to UI users.
- Catch expected DB errors (uniqueness/FK/integrity) and return clear messages.
- Log unexpected exceptions with actionable context.
- In states, fail safely (set error state or return) instead of crashing page events.

### Security

- Use bcrypt from `editorial_cms/core/security.py` for password hashing/verification.
- Never store plaintext passwords.
- Enforce role checks in three places where relevant:
  1) state mutation methods,
  2) page `on_load` guards,
  3) UI visibility/controls.

### SQLModel and Querying

- Use `with Session(engine) as session:` for all DB access.
- Query with `select(...)` + `session.exec(...)`; avoid raw SQL.
- `commit()` after mutations; `refresh()` when returning newly created records.
- Use eager loading (`selectinload`) where N+1 risk exists.
- Keep slugs unique; collision pattern should append counters (`slug`, `slug-1`, ...).

### Reflex State and Pages

- Prefer `async def` for state event handlers.
- Use `await self.get_state(OtherState)` for cross-state access.
- Reset form fields after successful create/update actions.
- Use `@rx.var` for computed properties.
- In pages, preload auth/data in `@rx.page(..., on_load=[...])`.
- Prefer `rx.foreach` and `rx.cond` over ad-hoc Python rendering logic.

### Components

- Component functions should return `rx.Component`.
- Shared layouts (admin/public wrappers) belong in `editorial_cms/components/`.
- Keep UI pieces composable and avoid large monolithic component functions when possible.

## Repository Layout (Current)

```text
editorial_cms/
  models/
  services/
  states/
  pages/admin/
  pages/public/
  components/
  core/
  database.py
  editorial_cms.py
```

## Agent Workflow Expectations

- Before coding, inspect neighboring files for local conventions.
- Prefer minimal, targeted changes over broad refactors.
- If adding tests, place them under `tests/` mirroring package structure.
- When touching DB behavior, verify both service logic and state/page integrations.
- If introducing new dependency/tooling, document command usage in this file.

## Cursor and Copilot Rules

- Cursor rules sources checked:
  - `.cursor/rules/` -> not present
  - `.cursorrules` -> not present
- Copilot rules source checked:
  - `.github/copilot-instructions.md` -> not present
  - `copilot-instructions.md` (repo root) -> present and should be treated as authoritative supplemental guidance.

When guidance conflicts, use this priority:
1. Explicit user request
2. `AGENTS.md`
3. `copilot-instructions.md`
4. Existing local code patterns in touched files
