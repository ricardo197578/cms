# AGENTS.md - Editorial CMS

Operating guide for coding agents working in this repository.

## Project Snapshot
- Stack: Python 3.x, Reflex `0.8.27`, SQLModel, PostgreSQL, `python-dotenv`, bcrypt.
- Main package: `editorial_cms/`.
- Architecture: models -> services -> states -> pages/components.
- Domain language is mostly Spanish (`Usuario`, `categoria`, `rol`, `titulo`).
- `DATABASE_URL` is loaded from `.env` in `editorial_cms/database.py`.
- `init_db()` is called on startup in `editorial_cms/editorial_cms.py`.

## Environment Setup
Use local `venv` when available.

```bash
# Windows PowerShell
.\venv\Scripts\Activate.ps1

# Windows CMD
venv\Scripts\activate.bat

# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Build, Lint, and Test Commands
```bash
# Run app (dev)
reflex run

# Run app on custom port
reflex run --port 3000

# Build/deploy bundle
reflex deploy

# Lint (ruff is not pinned in requirements)
pip install ruff
ruff check .
ruff check --fix .

# Optional formatting
ruff format .

# Install test tooling
pip install pytest pytest-asyncio

# Run full test suite
pytest

# Run a single test file
pytest tests/test_post_service.py

# Run a single test function (preferred single-test pattern)
pytest tests/test_post_service.py::test_crear_post

# Run tests by keyword
pytest -k "post and crear"

# Stop on first failure
pytest -x
```

Notes:
- A `tests/` directory may not exist yet; create it for new tests.
- If no tests are collected, run lint and verify app boot (`reflex run`).

## Database and Migrations
- No `alembic.ini` or migration folder is currently present.
- If migrations are introduced, use:

```bash
alembic upgrade head
alembic revision --autogenerate -m "descripcion"
```

## Code Style Guidelines

### Naming and Language
- Keep domain/business names in Spanish unless extending an existing English API.
- Modules/files: `snake_case`.
- Classes: `PascalCase`.
- Functions/methods/variables: `snake_case`.
- State classes end with `State`.
- Service functions follow CRUD verbs: `crear_*`, `obtener_*`, `actualizar_*`, `eliminar_*`.

### Imports
- Prefer absolute imports from `editorial_cms.*`.
- Group imports: stdlib, third-party, local; keep one blank line between groups.
- Use `TYPE_CHECKING` imports for model circular references where needed.

### Formatting
- Follow PEP 8 and keep functions small and cohesive.
- Prefer focused service helpers over large multi-purpose functions.
- Extract reusable logic (slug generation, auth checks, filtering) into service/helpers.

### Types
- Add type hints to public function parameters and return values.
- Use `T | None` (or `Optional[T]`) consistently for nullable values.
- Type SQLModel fields explicitly (including nullable foreign keys).
- Type Reflex state fields (`str`, `int`, `list[Post]`, etc.).

### SQLModel and Data Access
- Use `with Session(engine) as session:` for every DB operation.
- Use `select(...)` + `session.exec(...)`; avoid raw SQL.
- Call `session.commit()` after mutations.
- Call `session.refresh(obj)` when returning newly created rows.
- Keep slug uniqueness with suffix collisions (`slug`, `slug-1`, `slug-2`).

### Reflex State and Pages
- Prefer `async def` for state event handlers.
- Use `await self.get_state(OtherState)` for cross-state access.
- Guard protected actions with auth/role checks before mutation.
- Reset form fields after successful create/update flows.
- Use `@rx.var` for computed reactive properties.
- Prefer `rx.foreach` and `rx.cond` for list/conditional UI rendering.

### Components
- Component functions should return `rx.Component`.
- Keep components composable; avoid monolithic page-sized functions.
- Shared wrappers/layouts belong in `editorial_cms/components/`.

### Error Handling and Security
- Never expose raw stack traces or exceptions to end users.
- Catch expected DB errors (integrity, uniqueness, FK) and return clear messages.
- In states, fail safely by setting error state or returning early.
- Log unexpected exceptions with actionable context.
- Use password helpers from `editorial_cms/core/security.py`.
- Never store plaintext passwords.
- Enforce role checks in state methods, page guards, and UI visibility.

## Testing Guidance
- Add tests under `tests/` mirroring the package layout.
- Prioritize service-layer CRUD/auth tests first.
- Add regression tests when fixing bugs.
- Use `pytest-asyncio` for async state logic.
- Minimum PR verification for code changes: lint + targeted tests.

## Agent Workflow Expectations
- Inspect nearby files before editing to match local patterns.
- Prefer minimal, targeted edits over broad refactors.
- Do not rename Spanish domain entities to English without strong reason.
- When changing DB behavior, verify service plus state/page integration.
- If adding tools/dependencies, update this file with commands.

## Cursor and Copilot Rules
Checked sources in this repository:
- `.cursor/rules/` -> not present
- `.cursorrules` -> not present
- `.github/copilot-instructions.md` -> not present
- `copilot-instructions.md` -> present and should be followed as supplemental guidance

Conflict priority:
1. Explicit user request
2. `AGENTS.md`
3. `copilot-instructions.md`
4. Existing local code conventions in touched files
