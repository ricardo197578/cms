# Editorial CMS Coding Instructions

You are assisting with an Editorial CMS built with **Python, Reflex framework, SQLModel ORM, and PostgreSQL**. This document defines the architectural patterns, naming conventions, and best practices for the project.

## Project Overview

- **Stack**: Python 3.x, Reflex (React-like framework), SQLModel (Pydantic + SQLAlchemy hybrid), PostgreSQL (Neon)
- **Language**: Spanish (code uses Spanish entity names and comments)
- **Architecture**: Clean separation between models → services → states → pages + components
- **Scope**: Editorial CMS with user management, post authoring, categories, role-based admin panel, and public article viewing

## Naming Conventions

When creating files, classes, functions, or database entities, follow these rules:

### Files & Modules
- Use **snake_case** for all Python files and module names
- Examples: `post_service.py`, `auth_state.py`, `categoria_sidebar.py`
- Never use CamelCase or SCREAMING_SNAKE_CASE for filenames

### Classes
- Use **PascalCase** for all class names
- Database models: `Usuario`, `Post`, `Categoria` (not `usuario`, `post`, `categoria`)
- Reflex state classes: Must end with `State` (e.g., `AuthState`, `PostState`, `PublicState`)
- UI components: Descriptive camelCase with `rx.Component` return type (e.g., `admin_header()` → component function)

### Functions & Methods
- Use **snake_case** for all functions and methods
- Naming patterns:
  - **Service functions**: `crear_*()`, `obtener_*()`, `eliminar_*()`, `actualizar_*()` (Spanish verbs matching business operations)
  - **Reflex state methods**: Async by default, e.g., `async def cargar_posts(self):`, `async def guardar_post(self):`
  - **Helper functions**: Descriptive verbs like `generar_slug_unico()`, `hash_password()`, `verificar_password()`

### Database Entities & Variables
- Use **Spanish names** for domain entities: `usuario`, `post`, `categoria`, `rol`
- Use **snake_case** for fields and variable names

## Architecture Patterns

### 1. Models Layer (`editorial_cms/models/`)

All data entities use **SQLModel** with explicit constraints:

```python
from typing import Optional
from sqlmodel import SQLModel, Field

class Usuario(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True, min_length=3)
    email: str = Field(unique=True)
    password_hash: str
    rol: str = Field(default="autor")  # superadmin, admin, editor, autor
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
```

**Key Patterns**:
- Use `Optional[Type]` for nullable fields
- Always specify `primary_key=True` for ID
- Use `Field(index=True)` for frequently searched fields
- Use `Field(unique=True)` for unique constraints
- Timestamps: `Field(default_factory=datetime.utcnow)` (never `default=datetime.utcnow()`)
- Use `Relationship()` for foreign key relationships with lazy loading when needed
- Never expose raw SQL queries; rely on SQLModel's ORM

### 2. Service Layer (`editorial_cms/services/`)

All business logic is encapsulated in service modules with **session management**:

```python
from sqlmodel import Session, select
from editorial_cms.database import engine

def crear_post(titulo: str, contenido: str, autor_id: int, categoria_id: int) -> Post:
    """Create a new post and ensure slug uniqueness."""
    with Session(engine) as session:
        slug = generar_slug_unico(titulo, session)
        nuevo_post = Post(
            titulo=titulo,
            contenido=contenido,
            slug=slug,
            autor_id=autor_id,
            categoria_id=categoria_id
        )
        session.add(nuevo_post)
        session.commit()
        session.refresh(nuevo_post)
        return nuevo_post

def obtener_posts_por_categoria(categoria_id: int) -> List[Post]:
    """Fetch posts with relationships eagerly loaded."""
    with Session(engine) as session:
        statement = (
            select(Post)
            .where(Post.categoria_id == categoria_id)
            .options(selectinload(Post.autor))  # Prevent N+1
        )
        return session.exec(statement).all()
```

**Key Patterns**:
- Wrap all database operations in `with Session(engine):` context manager
- Use `session.exec(select(...))` for queries, never raw SQL
- Always `session.commit()` after mutations
- Always `session.refresh(obj)` after creation to get auto-generated IDs
- Use `selectinload()` for related entities to avoid N+1 queries
- Function names follow CRUD pattern: `crear_*`, `obtener_*`, `actualizar_*`, `eliminar_*`
- Return models from service functions, not raw tuples
- Centralize slug generation with uniqueness validation in service logic

### 3. State Layer (`editorial_cms/states/`)

Reflex states manage UI state and coordinate with services:

```python
import reflex as rx
from editorial_cms.services.post_service import crear_post, obtener_posts
from editorial_cms.models import Post

class PostState(rx.State):
    """Manages post-related UI and application state."""
    titulo: str = ""
    contenido: str = ""
    posts: list[Post] = []
    
    async def cargar_posts(self):
        """Fetch posts from service and update state."""
        self.posts = obtener_posts()  # Service call, may be async if needed
    
    async def guardar_post(self):
        """Create a new post if user is authenticated."""
        auth = await self.get_state(AuthState)
        if not auth.usuario_id:
            return  # Unauthorized
        crear_post(
            titulo=self.titulo,
            contenido=self.contenido,
            autor_id=auth.usuario_id
        )
        self.titulo = ""
        self.contenido = ""
        await self.cargar_posts()  # Reload after creation
    
    @rx.var
    def titulo_valido(self) -> bool:
        """Computed property for validation."""
        return len(self.titulo) >= 5
```

**Key Patterns**:
- All state methods are `async def` even if they synchronously call services
- Access other states via `await self.get_state(OtherState)`
- Always check authentication before mutating user-owned data
- Use `@rx.var` for computed properties (cached, reactive in UI)
- Clear form fields after successful operations
- Reload lists after mutations (reload all related UI)
- Use type hints for all state variables

### 4. Pages Layer (`editorial_cms/pages/`)

Pages are route handlers that compose layouts and state:

```python
import reflex as rx
from editorial_cms.pages.admin_layout import admin_layout
from editorial_cms.states.auth_state import AuthState
from editorial_cms.states.post_state import PostState

@rx.page(
    route="/admin/posts",
    on_load=[AuthState.check_auth, PostState.cargar_posts],
    title="Posts"
)
def posts_page() -> rx.Component:
    """Admin posts page with authorization."""
    return admin_layout(
        rx.vstack(
            rx.heading("Gestión de Posts"),
            rx.text_area(
                value=PostState.titulo,
                on_change=PostState.set_titulo,
                placeholder="Título..."
            ),
            rx.button(
                "Guardar Post",
                on_click=PostState.guardar_post,
                is_disabled=~PostState.titulo_valido
            ),
            rx.foreach(PostState.posts, post_row),
        )
    )
```

**Key Patterns**:
- Use `@rx.page()` decorator with `route`, `on_load`, and `title`
- `on_load` array runs security checks and preloads data before rendering
- Always wrap admin pages with `admin_layout()`
- Bind state changes with `on_change=StateName.set_fieldname` (auto-generated setter)
- Use `rx.foreach()` for lists (not comprehensions)
- Use `rx.cond()` for conditional rendering based on state

### 5. Components Layer (`editorial_cms/components/`)

Reusable UI components are functions that return `rx.Component`:

```python
import reflex as rx
from editorial_cms.states.auth_state import AuthState

def admin_header() -> rx.Component:
    """Admin header with user info and logout."""
    return rx.hstack(
        rx.heading("Editorial CMS", size="lg"),
        rx.spacer(),
        rx.text(AuthState.usuario_nombre),
        rx.button("Logout", on_click=AuthState.logout),
        width="100%",
        padding="15px",
        border_bottom="1px solid #e0e0e0"
    )

def admin_layout(content: rx.Component) -> rx.Component:
    """Wraps content with sidebar + header layout."""
    return rx.hstack(
        admin_sidebar(),
        rx.vstack(
            admin_header(),
            rx.box(content, padding="25px", flex="1"),
        ),
        width="100%",
        height="100vh"
    )
```

**Key Patterns**:
- Component functions have no arguments or accept `rx.Component` for composability
- Always return `rx.Component` type hint
- Layouts are functions that wrap content, promoting reuse
- Use `rx.hstack()` for horizontal layouts, `rx.vstack()` for vertical
- Leverage spacing components like `rx.spacer()` for alignment

## Security & Authentication Patterns

### Password Management
Always use bcrypt with salt (in `core/security.py`):

```python
import bcrypt

def hash_password(password: str) -> str:
    """Hash password with automatic salt generation."""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def verify_password(password: str, hashed: str) -> bool:
    """Verify plaintext password against hashed value."""
    return bcrypt.checkpw(password.encode(), hashed.encode())
```

**Never store plaintext passwords.** Always `.encode()`/`.decode()` for bcrypt binary compatibility.

### Role-Based Authorization
Four-tier role hierarchy with cascading permission checks:
- **superadmin**: Full system access
- **admin**: Can manage users, posts, categories
- **editor**: Can publish posts, moderate comments
- **autor**: Can draft posts (no publish)

Check roles at **three layers**:
1. **State method layer**: Guard state changes
2. **Page load layer**: Block unauthorized route access via `on_load=[AuthState.check_auth]`
3. **UI layer**: Conditionally render components

```python
# Always check before mutations
if user_role not in ["superadmin", "admin"]:
    raise PermissionError("Only admins can delete posts")
```

## Best Practices

### Data Validation
- Use SQLModel's `Field()` constraints: `min_length`, `max_length`, `regex`
- Validate inputs in service layer before persistence
- Return meaningful error messages to UI

### Async/Await
- All Reflex state methods should be `async def`
- Await cross-state access: `auth = await self.get_state(AuthState)`
- Do **not** make blocking database calls without wrapping in async context

### Query Optimization
- **Always eager-load related entities** using `selectinload()` to prevent N+1
- Index frequently searched columns: `Field(index=True)`
- Use pagination for large result sets
- Cache computed properties with `@rx.var`

### Error Handling
- Catch database integrity errors (uniqueness, foreign key violations)
- Return clear user-facing messages, not raw exceptions
- Log errors for debugging; never expose stack traces to UI

### Slug Generation
- Slugs must be **unique and indexed**
- Auto-number on collision: `my-post`, `my-post-1`, `my-post-2`
- Convert to lowercase, remove special characters
- Used for URL-friendly post identifiers

### Testing
- Consider adding `pytest` + `pytest-asyncio` fixtures for service layer
- Mock database sessions with in-memory SQLite
- Test state logic with state snapshots

## File Organization

```
editorial_cms/
├── models/              # Data models (SQLModel)
├── services/            # Business logic (database + operations)
├── states/              # Reflex state management
├── pages/
│   ├── admin/           # Protected admin routes
│   └── public/          # Public-facing routes
├── components/          # Reusable UI components
├── core/                # Security, utilities
├── database.py          # Database engine + session
├── editorial_cms.py     # App initialization
└── __init__.py
```

## When Asking for Help

Mention:
- **What layer**: models, services, states, pages, or components?
- **Pattern conflict**: What existing pattern are you trying to follow?
- **Use case**: What business operation are you implementing? (CRUD, auth, etc.)
- **Context**: Which entity (Usuario, Post, Categoria, etc.) are you working with?
