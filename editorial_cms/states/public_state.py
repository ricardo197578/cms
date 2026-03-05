import reflex as rx
from typing import Optional, List
from editorial_cms.models.post import Post
from editorial_cms.services.post_service import (
    obtener_post_por_id,
    obtener_publicados,
)


class PublicState(rx.State):

    posts: List[Post] = []
    post_actual: Optional[Post] = None

    # 🔹 Cargar solo artículos publicados
    async def cargar_publicados(self):
        self.posts = obtener_publicados()

    # 🔹 Ver detalle de artículo
    async def ver_post(self, post_id: int):
        try:
            post_id = int(post_id)
            self.post_actual = obtener_post_por_id(post_id)
            return rx.redirect("/articulo")
        except Exception:
            self.post_actual = None