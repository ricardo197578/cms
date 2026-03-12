import reflex as rx
from editorial_cms.services.category_service import (
    crear_categoria,
    obtener_categorias,
    actualizar_categoria,
    eliminar_categoria,
)
from editorial_cms.models.category import Category
from editorial_cms.states.auth_state import AuthState


class CategoriaAdminState(rx.State):

    # 🔹 Formulario
    nombre: str = ""
    mensaje: str = ""

    # 🔹 Datos
    categorias: list[Category] = []

    # 🔹 Edición
    editando_id: int | None = None

    # 🔹 Eliminación
    categoria_a_eliminar: int | None = None
    nombre_categoria_eliminar: str = ""
    mostrar_confirmacion: bool = False

    # ------------------------------------------------

    async def cargar(self):
        auth = await self.get_state(AuthState)

        if auth.user_role != "admin":
            return

        self.categorias = obtener_categorias()

    # ------------------------------------------------

    async def crear(self):

        auth = await self.get_state(AuthState)

        if auth.user_role != "admin":
            self.mensaje = "No tiene permisos"
            return

        if not self.nombre.strip():
            self.mensaje = "Debe ingresar un nombre"
            return

        crear_categoria(self.nombre.strip())

        self.nombre = ""
        self.mensaje = "Categoría creada ✓"

        await self.cargar()

    # ------------------------------------------------

    def set_editando(self, categoria_id: int):

        categoria = next(
            (c for c in self.categorias if c.id == categoria_id),
            None
        )

        if categoria:
            self.editando_id = categoria_id
            self.nombre = categoria.nombre

    # ------------------------------------------------

    async def actualizar(self):

        auth = await self.get_state(AuthState)

        if auth.user_role != "admin":
            self.mensaje = "No tiene permisos"
            return

        if not self.nombre.strip():
            self.mensaje = "Nombre no puede estar vacío"
            return

        if self.editando_id is None:
            return

        resultado = actualizar_categoria(
            self.editando_id,
            self.nombre.strip()
        )

        if resultado:
            self.mensaje = "Categoría actualizada ✓"
            self.nombre = ""
            self.editando_id = None
        else:
            self.mensaje = "Error al actualizar"

        await self.cargar()

    # ------------------------------------------------

    def cancelar_edicion(self):
        self.editando_id = None
        self.nombre = ""
        self.mensaje = ""

    # ------------------------------------------------

    def preparar_eliminacion(self, categoria_id: int):

        categoria = next(
            (c for c in self.categorias if c.id == categoria_id),
            None
        )

        if categoria:
            self.categoria_a_eliminar = categoria.id
            self.nombre_categoria_eliminar = categoria.nombre
            self.mostrar_confirmacion = True

    # ------------------------------------------------

    async def confirmar_eliminacion(self):

        auth = await self.get_state(AuthState)

        if auth.user_role != "admin":
            return

        if self.categoria_a_eliminar is None:
            return

        if eliminar_categoria(self.categoria_a_eliminar):
            self.mensaje = "Categoría eliminada ✓"
        else:
            self.mensaje = "Error al eliminar"

        self.categoria_a_eliminar = None
        self.nombre_categoria_eliminar = ""
        self.mostrar_confirmacion = False

        await self.cargar()

    # ------------------------------------------------

    def cancelar_eliminacion(self):

        self.categoria_a_eliminar = None
        self.nombre_categoria_eliminar = ""
        self.mostrar_confirmacion = False