import reflex as rx
from typing import Optional, List
from editorial_cms.models.post import Post
from editorial_cms.services.post_service import (
    obtener_post_por_id,
    obtener_publicados,
    obtener_post_por_slug,
    obtener_posts_por_categoria_slug,
)
from editorial_cms.services.category_service import (
    obtener_categoria_por_slug,
)


class PublicState(rx.State):

    posts: List[Post] = []
    post_actual: Optional[Post] = None

    # 🔹 NUEVO: para filtrado por categoría
    posts_categoria: List[Post] = []
    nombre_categoria_actual: str = ""

    # 🔹 Cargar solo artículos publicados
    async def cargar_publicados(self):
        self.posts = obtener_publicados()

    # 🔹 Cargar artículo por slug
    async def cargar_por_slug(self):
        slug = self.router.page.params.get("slug")

        print("SLUG DESDE STATE:", slug)

        if not slug:
            self.post_actual = None
            return

        self.post_actual = obtener_post_por_slug(slug)

    # 🔹 NUEVO: cargar posts por categoría
    async def cargar_posts_por_categoria_slug(self):
        slug = self.router.page.params.get("slug")

        print("CATEGORIA SLUG:", slug)

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

    # 🔹 Ver detalle de artículo
    async def ver_post(self, post_id: int):
        try:
            post_id = int(post_id)
            self.post_actual = obtener_post_por_id(post_id)
            return rx.redirect("/articulo")
        except Exception:
            self.post_actual = None