import reflex as rx
from editorial_cms.states.auth_state import AuthState
from editorial_cms.states.post_state import PostState
from editorial_cms.components.admin_layout import admin_layout


@rx.page(
    route="/admin/posts",
    on_load=[AuthState.check_auth, PostState.cargar_posts]
)
def posts():

    contenido = rx.vstack(
        rx.heading("Gestión de Artículos"),

        rx.input(
            placeholder="Título",
            value=PostState.titulo,
            on_change=PostState.set_titulo
        ),

        rx.text_area(
            placeholder="Contenido",
            value=PostState.contenido,
            on_change=PostState.set_contenido
        ),

        rx.button(
            "Guardar",
            on_click=lambda: PostState.guardar_post(AuthState.user_id)
        ),

        rx.divider(),

        rx.foreach(
            PostState.posts,
            lambda post: rx.box(
                rx.heading(post.titulo),
                rx.text(post.contenido),
                border="1px solid #ddd",
                padding="10px",
            )
        ),
    )

    return admin_layout(contenido)