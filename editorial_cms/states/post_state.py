import reflex as rx
from typing import List
from editorial_cms.models.post import Post
from editorial_cms.models.category import Category
from editorial_cms.states.auth_state import AuthState
from editorial_cms.services.post_service import (
    crear_post,
    obtener_posts,
    obtener_posts_por_autor,
    eliminar_post,
    actualizar_post,
    obtener_post_por_id,
)
from editorial_cms.services.post_service import toggle_publicado
from editorial_cms.services.category_service import obtener_categorias


class PostState(rx.State):

    titulo: str = ""
    contenido: str = ""
    categoria_id: str = ""

    posts: List[Post] = []
    categorias: List[Category] = []
    editando_id: int | None = None

    
    # 🔹 Cargar posts según rol
    async def cargar_posts(self):

        auth = await self.get_state(AuthState)

        # Admin → todos
        if auth.user_role == "admin":
            self.posts = obtener_posts()
            return

        # Editor → solo los suyos
        if auth.user_id:
            self.posts = obtener_posts_por_autor(auth.user_id)
        else:
            self.posts = []

    # 🔹 Cargar categorías disponibles
    async def cargar_categorias(self):
        self.categorias = obtener_categorias()

    # 🔹 Crear post seguro
    async def guardar_post(self):

        if not self.titulo or not self.contenido:
            return

        auth = await self.get_state(AuthState)

        if not auth.user_id:
            return

        crear_post(self.titulo, self.contenido, auth.user_id,int(self.categoria_id))

        self.titulo = ""
        self.contenido = ""
        
        await self.cargar_posts()

    # 🔹 Eliminar (solo admin)
    async def eliminar_post(self, post_id: int):

        auth = await self.get_state(AuthState)

        if auth.user_role != "admin":
            return

        eliminar_post(post_id)
        await self.cargar_posts()

    # 🔹 Preparar edición
    def set_editando(self, post_id: int):

        post = next((p for p in self.posts if p.id == post_id), None)

        if not post:
            return

        self.editando_id = post_id
        self.titulo = post.titulo
        self.contenido = post.contenido

    # 🔹 Actualizar post con control por autor
    async def actualizar_post(self):

        if not self.editando_id:
            return

        auth = await self.get_state(AuthState)

        post = obtener_post_por_id(self.editando_id)

        if not post:
            return

        # Si no es admin, solo puede editar si es autor
        if auth.user_role != "admin":
            if post.autor_id != auth.user_id:
                return

        actualizar_post(self.editando_id, self.titulo, self.contenido)

        self.titulo = ""
        self.contenido = ""
        self.editando_id = None

        await self.cargar_posts()

    async def toggle_publicado(self, post_id: int):

        toggle_publicado(post_id)
        await self.cargar_posts()