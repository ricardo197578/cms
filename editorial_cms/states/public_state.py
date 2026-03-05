import reflex as rx
from typing import Optional
from editorial_cms.models.post import Post
from editorial_cms.services.post_service import obtener_post_por_id


class PublicState(rx.State):

    post_actual: Optional[Post] = None

    def ver_post(self, post_id):
        try:
            post_id = int(post_id)
            self.post_actual = obtener_post_por_id(post_id)
            return rx.redirect("/articulo")
        except Exception:
            self.post_actual = None