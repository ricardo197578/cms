import reflex as rx
from editorial_cms.states.public_state import PublicState


@rx.page(
    route="/articulos",
    on_load=[
        PublicState.cargar_publicados,
        PublicState.cargar_categorias_sidebar,
        PublicState.cargar_recientes,
    ],
)
def articulos():

    return rx.container(

        rx.hstack(

            # 🔹 CONTENIDO PRINCIPAL
            rx.box(
                rx.vstack(
                    rx.heading("Artículos", size="6"),
                    rx.link("← Volver", href="/"),
                    
                    rx.cond(
                        PublicState.posts,
                        rx.foreach(
                            PublicState.posts,
                            lambda post: rx.box(
                                rx.vstack(                                                                                                       
                                    rx.heading(post.titulo, size="4"),
                                    rx.text(
                                        post["fecha_publicacion"],
                                        font_size="sm",
                                        color="gray",
                                    ),
                                    rx.text(post.contenido[:120] + "..."),   

                                    rx.link(
                                        "Leer más",
                                        href="/articulo/" + post.slug,
                                    ),
                                    spacing="2",
                                    align="start",
                                ),
                                padding="1em",
                                border="1px solid #eee",
                                border_radius="8px",
                                width="100%",
                            ),
                        ),
                        rx.heading("No hay artículos publicados"),
                    ),

                    spacing="4",
                    align="start",
                    width="100%",
                ),
                width="70%",
            ),

            # 🔹 SIDEBAR
            rx.box(
                rx.vstack(
                    rx.heading("Recientes", size="4"),

                    rx.foreach(
                        PublicState.recientes,
                        lambda post: rx.link(
                            post.titulo,
                            href="/articulo/" + post.slug,
                            font_size="sm",
                        ),
                    ),

                    rx.divider(),
                    
                    rx.heading("Categorías", size="4"),

                    rx.foreach(
                        PublicState.categorias_sidebar,
                        lambda cat: rx.hstack(
                            rx.link(
                                cat.nombre,
                                href="/categoria/" + cat.slug,
                            ),
                            rx.spacer(),
                            rx.badge(cat.cantidad),
                            width="100%",
                        ),
                    ),

                    spacing="3",
                    align="start",
                ),
                width="30%",
                padding_left="2em",
            ),

            align="start",
            width="100%",
        ),

        padding="2em",
        max_width="1100px",
    )