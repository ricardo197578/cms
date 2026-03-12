import reflex as rx
from editorial_cms.states.auth_state import AuthState
from editorial_cms.states.post_state import PostState
from editorial_cms.components.admin_layout import admin_layout

@rx.page(
    route="/admin/posts",
    on_load=[AuthState.check_auth, PostState.cargar_posts, PostState.cargar_categorias]
)
def posts():

    contenido = rx.vstack(

        # HEADER DE LA PÁGINA
        rx.flex(
            rx.heading("Gestión de Artículos", size="8"),

            rx.badge(
                PostState.posts.length().to_string() + " Total",
                variant="surface",
                color_scheme="indigo"
            ),

            spacing="4",
            align="center",
            margin_bottom="4",
        ),

        # =========================
        # EDITOR DE ARTÍCULOS
        # =========================
        rx.card(

            rx.vstack(

                rx.hstack(
                    rx.icon("pen-line"),
                    rx.text("Editor de Contenido", weight="bold"),
                    spacing="2",
                ),

                rx.select.root(
                    rx.select.trigger(
                        placeholder="Seleccionar categoría",
                        width="100%"
                    ),
                    rx.select.content(
                        rx.foreach(
                            PostState.categorias,
                            lambda cat: rx.select.item(cat.nombre, value=str(cat.id))
                        )
                    ),
                    on_change=PostState.set_categoria_id,
                ),

                rx.input(
                    placeholder="Título del artículo...",
                    value=PostState.titulo,
                    on_change=PostState.set_titulo,
                    width="100%",
                    size="3",
                ),

                rx.vstack(
                    rx.text("Contenido del artículo", weight="bold"),
                    
                    # USO DEL EDITOR
                    rx.text_area(
                        placeholder="Escribe el contenido del artículo...",
                        value=PostState.contenido,
                        on_change=PostState.set_contenido,
                        width="100%",
                        min_height="250px",
                    ),
                   
                    width="100%",
                ),

                rx.flex(

                    rx.cond(
                        PostState.editando_id,

                        rx.button(
                            "Actualizar Artículo",
                            icon="refresh-cw",
                            color_scheme="blue",
                            on_click=PostState.actualizar_post,
                            width="100%"
                        ),

                        rx.button(
                            "Publicar Nuevo",
                            icon="plus",
                            color_scheme="grass",
                            on_click=PostState.guardar_post,
                            width="100%"
                        ),
                    ),

                    width="100%",
                ),

                spacing="3",
            ),

            width="100%",
            padding="6",
            variant="surface",
        ),

        rx.divider(margin_y="4"),

        # =========================
        # TABLA DE ARTÍCULOS
        # =========================
        rx.card(

            rx.table.root(

                rx.table.header(
                    rx.table.row(

                        rx.table.column_header_cell("Título"),

                        rx.table.column_header_cell("Estado"),

                        rx.table.column_header_cell("Acciones"),
                    )
                ),

                rx.table.body(

                    rx.foreach(

                        PostState.posts,

                        lambda post: rx.table.row(

                            # TÍTULO
                            rx.table.cell(
                                rx.vstack(
                                    rx.text(
                                        post.titulo,
                                        weight="bold"
                                    ),

                                    rx.text(
                                        post.contenido,
                                        size="2",
                                        color_scheme="gray",
                                        max_lines=1
                                    ),

                                    align_items="start",
                                )
                            ),

                            # ESTADO
                            rx.table.cell(

                                rx.cond(
                                    post.publicado,

                                    rx.badge(
                                        "Publicado",
                                        color_scheme="green",
                                        variant="soft"
                                    ),

                                    rx.badge(
                                        "Borrador",
                                        color_scheme="amber",
                                        variant="soft"
                                    ),
                                )
                            ),

                            # ACCIONES
                            rx.table.cell(

                                rx.hstack(

                                    rx.button(
                                        "Editar",
                                        icon="edit",
                                        size="1",
                                        variant="soft",
                                        on_click=lambda: PostState.set_editando(post.id)
                                    ),

                                    rx.button(
                                        rx.cond(
                                            post.publicado,
                                            "Desactivar",
                                            "Activar"
                                        ),
                                        size="1",
                                        variant="outline",
                                        color_scheme="blue",
                                        on_click=lambda: PostState.toggle_publicado(post.id)
                                    ),

                                    rx.cond(

                                        AuthState.usuario_logueado["rol"] == "admin",

                                        rx.button(
                                            "Eliminar",
                                            icon="trash-2",
                                            size="1",
                                            color_scheme="red",
                                            variant="soft",
                                            on_click=lambda: PostState.eliminar_post(post.id)
                                        ),
                                    )
                                )
                            )
                        )
                    )
                ),
                width="100%",
            ),
            width="100%",
        ),
        spacing="4",
        width="100%",
    )

    return admin_layout(contenido)
