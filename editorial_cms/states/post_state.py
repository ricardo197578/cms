import reflex as rx
from editorial_cms.services.post_service import crear_post, obtener_posts
from editorial_cms.services.post_service import eliminar_post
from editorial_cms.states.auth_state import AuthState
from typing import List
from editorial_cms.models.post import Post

class PostState(rx.State):

    titulo: str = ""
    contenido: str = ""

    posts: List[Post] = []

    def cargar_posts(self):
        self.posts = obtener_posts()

    def guardar_post(self, autor_id: int):
        self.posts = obtener_posts()

    def guardar_post(self, autor_id: int):
        if not self.titulo or not self.contenido:
            return

        crear_post(self.titulo, self.contenido, autor_id)

        self.titulo = ""
        self.contenido = ""

        self.cargar_posts()

    def eliminar_post(self, post_id: int):
        eliminar_post(post_id)
        self.cargar_posts()