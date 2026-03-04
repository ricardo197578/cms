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

        

        rx.cond(
        PostState.editando_id,
        rx.button(
            "Actualizar",
            color_scheme="blue",
            on_click=PostState.actualizar_post
        ),
        rx.button(
            "Guardar",
            on_click=PostState.guardar_post
        )
        ),

        rx.divider(),

        rx.foreach(
            PostState.posts,
            lambda post: rx.box(
                rx.vstack(
                    rx.heading(post.titulo),
                    rx.text(post.contenido),

                    rx.hstack(
                        rx.button(
                            "Editar",
                            size="1",
                            on_click=lambda: PostState.set_editando(post.id)
                        ),

                        rx.cond(
                            AuthState.usuario_logueado["rol"] == "admin",
                            rx.button(
                                "Eliminar",
                                color_scheme="red",
                                size="1",
                                on_click=lambda: PostState.eliminar_post(post.id)
                            )
                        ),

                        spacing="2",
                    ),

                    spacing="2",
                    align_items="start",
                ),
                border="1px solid #ddd",
                padding="10px",
                border_radius="8px",
            )
        )
    )

    return admin_layout(contenido)