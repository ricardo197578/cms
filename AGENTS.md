# AGENTS.md - Editorial CMS
Operational guide for agentic coding assistants working in this repository.

## Project Snapshot
- Stack: Python 3.x, Reflex `0.8.27`, SQLModel, PostgreSQL, `python-dotenv`, bcrypt.
- Main package: `editorial_cms/`.
- Runtime entrypoint: `editorial_cms/editorial_cms.py` (calls `init_db()` at startup).
- Data access: SQLModel sessions from `editorial_cms/database.py` using `DATABASE_URL`.
- Architecture flow: `models -> services -> states -> pages/components`.
- Domain language is Spanish (`Usuario`, `Category`, `rol`, `titulo`, `categoria_id`, etc.).

## Environment Setup
Use the local virtual environment when available.

```bash
# Windows PowerShell
.\venv\Scripts\Activate.ps1

# Windows CMD
venv\Scripts\activate.bat

# macOS/Linux
source venv/bin/activate

# Install runtime dependencies
pip install -r requirements.txt
```

## Build, Lint, and Test Commands
```bash
# Run app in dev mode
reflex run

# Build/deploy bundle
reflex deploy

# Install lint/test tools if missing
pip install ruff pytest pytest-asyncio

# Lint
ruff check .

# Lint with auto-fixes
ruff check --fix .

# Run all tests
pytest

# Run a single test file
pytest tests/test_post_service.py

# Run a single test function (preferred single-test pattern)
pytest tests/test_post_service.py::test_crear_post

# Run tests by keyword expression
pytest -k "post and crear"

# Stop at first failure
pytest -x
```

Notes:
- If `tests/` does not exist, create it and mirror package structure.
- If no tests are collected, run `ruff check .` and validate app boot with `reflex run`.

## Code Style Guidelines

### Naming and Language
- Keep business/domain names in Spanish unless extending an existing English API.
- Files/modules/functions/variables: `snake_case`.
- Classes: `PascalCase`; Reflex state classes must end in `State`.
- Service APIs should use CRUD-style Spanish verbs: `crear_*`, `obtener_*`, `actualizar_*`, `eliminar_*`.
- Prefer descriptive identifiers (`categoria_slug`, `imagen_destacada`, `user_role`) over abbreviations.

### Imports
- Prefer absolute imports from `editorial_cms.*`.
- Order imports by groups: stdlib, third-party, local.
- Keep imports at module top; avoid repeated imports inside functions unless needed for cycles.
- Remove unused imports while editing touched files.

### Formatting and Organization
- Follow PEP 8; keep functions focused and cohesive.
- Favor small helper functions (slugging, filtering, auth checks) over monolithic logic.
- Avoid broad refactors when a targeted change is sufficient.

### Types
- Add type hints to public function signatures and state fields.
- Use `T | None` (or `Optional[T]`) consistently for nullable values.
- Type SQLModel fields explicitly, including optional foreign keys.
- Prefer concrete containers in new code (`list[Post]`, `dict[str, str]`) over untyped collections.

## SQLModel and Persistence
- Always use `with Session(engine) as session:` for DB work.
- Prefer `select(...)` + `session.exec(...)`; avoid raw SQL.
- Call `session.commit()` after create/update/delete mutations.
- Call `session.refresh(obj)` when returning newly created/updated rows that need DB-generated fields.
- Keep slug generation deterministic and collision-safe (`slug`, `slug-1`, `slug-2`).

## Reflex State, Pages, and Components
- Prefer `async def` for state event handlers.
- Use `await self.get_state(OtherState)` for cross-state access.
- Enforce auth/role checks before protected mutations.
- Reset form fields after successful writes to avoid stale UI state.
- Use `@rx.var` for computed reactive properties.
- Prefer `rx.foreach` and `rx.cond` for list and conditional rendering.
- Component functions should return `rx.Component` and stay composable.
- Keep shared wrappers/layout primitives under `editorial_cms/components/`.

## Error Handling and Security
- Do not expose raw tracebacks to end users.
- Catch expected data errors (validation, uniqueness, FK integrity) and return actionable messages.
- In state handlers, fail safely (early return + set error state/message where appropriate).
- Log unexpected exceptions with enough context to debug.
- Use password helpers in `editorial_cms/core/security.py` (`hash_password`, `verify_password`).
- Never store plaintext passwords.
- Apply role checks in state methods, page guards, and UI visibility.

## Testing Guidance
- Put tests under `tests/` with paths mirroring `editorial_cms/`.
- Prioritize service-layer CRUD/auth tests first, then state-level regressions.
- Use `pytest-asyncio` for async state logic.
- Add regression tests when fixing bugs.
- Minimum verification for changes: lint + targeted tests for touched behavior.

## Database and Migrations
- Current repository does not include configured Alembic migration files.
- If migrations are introduced, use `alembic upgrade head` and `alembic revision --autogenerate -m "descripcion"`.

## Agent Workflow Expectations
- Inspect related files before editing to match local conventions.
- Prefer minimal, scoped edits over speculative rewrites.
- Do not rename Spanish domain entities to English without explicit reason.
- If changing DB behavior, verify service + state + page integration paths.
- If adding new tooling/dependencies, update this document with exact commands.

## Cursor and Copilot Rules
Checked sources in this repository:
- `.cursor/rules/`: not present
- `.cursorrules`: not present
- `.github/copilot-instructions.md`: not present
- `copilot-instructions.md`: present

How to apply them:
- Treat `copilot-instructions.md` as supplemental guidance for architecture and naming.
- If guidance conflicts, follow this priority order:
  1. Explicit user request
  2. `AGENTS.md`
  3. `copilot-instructions.md`
  4. Existing local conventions in touched files
