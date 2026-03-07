import reflex as rx
from typing import Optional, List
from editorial_cms.models.post import Post
from editorial_cms.models.categoria_sidebar import CategoriaSidebar
from editorial_cms.services.post_service import obtener_recientes


from editorial_cms.services.post_service import (
    obtener_post_por_id,
    obtener_publicados,
    obtener_post_por_slug,
    obtener_posts_por_categoria_slug,
)

from editorial_cms.services.category_service import (
    obtener_categoria_por_slug,
    obtener_categorias_con_contador,
)


class PublicState(rx.State):

    # 🔹 LISTADO GENERAL
    posts: List[Post] = []

    # 🔹 DETALLE
    post_actual: Optional[Post] = None

    # 🔹 SIDEBAR TIPADO CORRECTAMENTE
    categorias_sidebar: List[CategoriaSidebar] = []

    # 🔹 FILTRADO POR CATEGORÍA
    posts_categoria: List[Post] = []
    nombre_categoria_actual: str = ""

    recientes: List[Post] = []



    # =========================
    # CARGAS
    # =========================
    async def cargar_recientes(self):
        self.recientes = obtener_recientes()

    async def cargar_publicados(self):
        posts_db = obtener_publicados()

        for post in posts_db:
            post.fecha_publicacion = post.fecha_publicacion.strftime("%d/%m/%Y")

        self.posts = posts_db

    async def cargar_categorias_sidebar(self):
        self.categorias_sidebar = obtener_categorias_con_contador()

    async def cargar_por_slug(self):
        slug = self.router.page.params.get("slug")

        if not slug:
            self.post_actual = None
            return

        self.post_actual = obtener_post_por_slug(slug)

    async def cargar_posts_por_categoria_slug(self):
        slug = self.router.page.params.get("slug")

        if not slug:
            self.posts_categoria = []
            self.nombre_categoria_actual = ""
            return

        categoria = obtener_categoria_por_slug(slug)

        if categoria:
            self.nombre_categoria_actual = categoria.nombre
            self.posts_categoria = obtener_posts_por_categoria_slug(slug)
        else:
            self.posts_categoria = []
            self.nombre_categoria_actual = ""

    # =========================
    # NAVEGACIÓN
    # =========================

    async def ver_post(self, post_id: int):
        try:
            post_id = int(post_id)
            self.post_actual = obtener_post_por_id(post_id)
            return rx.redirect("/articulo")
        except Exception:
            self.post_actual = None