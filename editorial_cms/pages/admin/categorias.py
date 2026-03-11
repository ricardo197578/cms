import reflex as rx
from editorial_cms.services.category_service import (
    crear_categoria,
    obtener_categorias,
    actualizar_categoria,
    eliminar_categoria,
    obtener_categoria_por_id,
)
from editorial_cms.models.category import Category
from editorial_cms.components.admin_layout import admin_layout
from editorial_cms.states.auth_state import AuthState


class CategoriaAdminState(rx.State):
    """Estado para la gestión de categorías."""

    # Formulario
    nombre: str = ""
    mensaje: str = ""
    
    # Listas y control
    categorias: list[Category] = []
    editando_id: int | None = None
    categoria_a_eliminar: int | None = None
    mostrar_confirmacion: bool = False

    # 🔹 Cargar categorías
    async def cargar(self):
        auth = await self.get_state(AuthState)
        if auth.user_role != "admin":
            return
        self.categorias = obtener_categorias()

    # 🔹 Crear nueva categoría
    async def crear(self):
        auth = await self.get_state(AuthState)
        if auth.user_role != "admin":
            self.mensaje = "No tiene permisos"
            return

        if not self.nombre or not self.nombre.strip():
            self.mensaje = "Debe ingresar un nombre"
            return

        crear_categoria(self.nombre.strip())
        self.nombre = ""
        self.mensaje = "Categoría creada ✓"
        await self.cargar()

    # 🔹 Preparar edición
    def set_editando(self, categoria_id: int):
        categoria = next(
            (c for c in self.categorias if c.id == categoria_id), None
        )
        if categoria:
            self.editando_id = categoria_id
            self.nombre = categoria.nombre

    # 🔹 Actualizar categoría
    async def actualizar(self):
        auth = await self.get_state(AuthState)
        if auth.user_role != "admin":
            self.mensaje = "No tiene permisos"
            return

        if not self.nombre or not self.nombre.strip():
            self.mensaje = "Nombre no puede estar vacío"
            return

        if not self.editando_id:
            return

        resultado = actualizar_categoria(self.editando_id, self.nombre.strip())
        
        if resultado:
            self.mensaje = "Categoría actualizada ✓"
            self.nombre = ""
            self.editando_id = None
        else:
            self.mensaje = "Error al actualizar"
        
        await self.cargar()

    # 🔹 Cancelar edición
    def cancelar_edicion(self):
        self.editando_id = None
        self.nombre = ""
        self.mensaje = ""

    # 🔹 Preparar eliminación (mostrar confirmación)
    def preparar_eliminacion(self, categoria_id: int):
        self.categoria_a_eliminar = categoria_id
        self.mostrar_confirmacion = True

    # 🔹 Confirmar eliminación
    async def confirmar_eliminacion(self):
        auth = await self.get_state(AuthState)
        if auth.user_role != "admin":
            return

        if not self.categoria_a_eliminar:
            return

        if eliminar_categoria(self.categoria_a_eliminar):
            self.mensaje = "Categoría eliminada ✓"
        else:
            self.mensaje = "Error al eliminar"

        self.categoria_a_eliminar = None
        self.mostrar_confirmacion = False
        await self.cargar()

    # 🔹 Cancelar eliminación
    def cancelar_eliminacion(self):
        self.categoria_a_eliminar = None
        self.mostrar_confirmacion = False


@rx.page(
    route="/admin/categorias",
    on_load=CategoriaAdminState.cargar
)
def categorias():
    """Página de gestión de categorías con CRUD completo."""

    # Formulario para crear o editar
    formulario = rx.card(
        rx.vstack(
            # Título condicional
            rx.cond(
                CategoriaAdminState.editando_id,
                rx.hstack(
                    rx.icon("edit-2"),
                    rx.text("Editar Categoría", weight="bold"),
                    spacing="2",
                ),
                rx.hstack(
                    rx.icon("plus-circle"),
                    rx.text("Nueva Categoría", weight="bold"),
                    spacing="2",
                ),
            ),

            # Input
            rx.input(
                placeholder="Nombre de categoría...",
                value=CategoriaAdminState.nombre,
                on_change=CategoriaAdminState.set_nombre,
                width="100%",
                size="2",
            ),

            # Botones de acción
            rx.flex(
                rx.cond(
                    CategoriaAdminState.editando_id,
                    # Si está editando
                    rx.hstack(
                        rx.button(
                            "Actualizar",
                            icon="save",
                            color_scheme="blue",
                            on_click=CategoriaAdminState.actualizar,
                            width="100%",
                        ),
                        rx.button(
                            "Cancelar",
                            icon="x",
                            variant="outline",
                            color_scheme="gray",
                            on_click=CategoriaAdminState.cancelar_edicion,
                            width="100%",
                        ),
                        spacing="2",
                        width="100%",
                    ),
                    # Si está creando
                    rx.button(
                        "Crear Categoría",
                        icon="plus",
                        color_scheme="grass",
                        on_click=CategoriaAdminState.crear,
                        width="100%",
                    ),
                ),
                width="100%",
            ),

            # Mensaje de feedback
            rx.cond(
                CategoriaAdminState.mensaje != "",
                rx.box(
                    rx.text(CategoriaAdminState.mensaje, size="2"),
                    padding="3",
                    background=rx.cond(
                        CategoriaAdminState.mensaje.contains("✓"),
                        "#d1f2eb",
                        "#fef2f2",
                    ),
                    border_radius="8px",
                    border_left="4px solid",
                    border_left_color=rx.cond(
                        CategoriaAdminState.mensaje.contains("✓"),
                        "#059669",
                        "#dc2626",
                    ),
                ),
            ),

            spacing="4",
            width="100%",
        ),
        width="100%",
    )

    # Lista de categorías
    lista = rx.card(
        rx.vstack(
            rx.hstack(
                rx.icon("list"),
                rx.text("Categorías Registradas", weight="bold"),
                rx.badge(
                    CategoriaAdminState.categorias.length().to_string(),
                    color_scheme="blue",
                ),
                spacing="2",
                width="100%",
            ),

            rx.cond(
                CategoriaAdminState.categorias.length() > 0,
                rx.vstack(
                    rx.foreach(
                        CategoriaAdminState.categorias,
                        lambda cat: rx.hstack(
                            rx.box(
                                rx.vstack(
                                    rx.text(cat.nombre, weight="bold", size="3"),
                                    rx.text(
                                        cat.slug,
                                        size="1",
                                        color="#666",
                                    ),
                                    spacing="1",
                                ),
                                flex="1",
                            ),
                            rx.hstack(
                                rx.button(
                                    rx.icon("edit"),
                                    size="1",
                                    color_scheme="blue",
                                    variant="outline",
                                    on_click=lambda: CategoriaAdminState.set_editando(
                                        cat.id
                                    ),
                                ),
                                rx.button(
                                    rx.icon("trash-2"),
                                    size="1",
                                    color_scheme="red",
                                    variant="outline",
                                    on_click=lambda: CategoriaAdminState.preparar_eliminacion(
                                        cat.id
                                    ),
                                ),
                                spacing="2",
                            ),
                            padding="3",
                            border_bottom="1px solid #e5e7eb",
                            width="100%",
                            align="center",
                        ),
                    ),
                    width="100%",
                    spacing="0",
                ),
                rx.box(
                    rx.text("No hay categorías registradas", color="#999"),
                    padding="6",
                    text_align="center",
                ),
            ),
            spacing="4",
            width="100%",
        ),
        width="100%",
    )

    # Diálogo de confirmación
    dialogo = rx.dialog(
        rx.dialog.content(
            rx.vstack(
                rx.dialog.title("Confirmar eliminación"),
                rx.text("¿Está seguro que desea eliminar esta categoría?"),
                rx.text(
                    "Esta acción no se puede deshacer.",
                    size="1",
                    color="#666",
                ),
                rx.hstack(
                    rx.dialog.close(
                        rx.button(
                            "Cancelar",
                            variant="outline",
                            color_scheme="gray",
                        ),
                    ),
                    rx.button(
                        "Eliminar",
                        color_scheme="red",
                        on_click=CategoriaAdminState.confirmar_eliminacion,
                    ),
                    spacing="3",
                    width="100%",
                    justify="end",
                ),
                spacing="4",
            ),
        ),
        is_open=CategoriaAdminState.mostrar_confirmacion,
    )

    # Contenido principal
    contenido = rx.vstack(
        rx.heading("Gestión de Categorías", size="8"),

        formulario,
        lista,

        spacing="6",
        padding="2em",
        width="100%",
        max_width="800px",
    )

    return admin_layout(rx.vstack(contenido, dialogo, width="100%"))