import reflex as rx
from editorial_cms.services.post_service import crear_post, obtener_posts
from editorial_cms.services.post_service import eliminar_post
from editorial_cms.states.auth_state import AuthState
from editorial_cms.services.post_service import actualizar_post
from typing import List
from editorial_cms.models.post import Post

class PostState(rx.State):

    titulo: str = ""
    contenido: str = ""

    posts: List[Post] = []
    editando_id: int | None = None

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
    
    def set_editando(self, post_id: int):
        post = next(p for p in self.posts if p.id == post_id)

        self.editando_id = post_id
        self.titulo = post.titulo
        self.contenido = post.contenido

    def actualizar_post(self):
        if not self.editando_id:
            return

        actualizar_post(self.editando_id, self.titulo, self.contenido)

        self.titulo = ""
        self.contenido = ""
        self.editando_id = None

        self.cargar_posts()