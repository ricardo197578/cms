import reflex as rx
from editorial_cms.states.public_state import PublicState


@rx.page(
    route="/categoria/[slug]",
    on_load=PublicState.cargar_posts_por_categoria_slug,
)
def categoria():

    return rx.container(
        rx.vstack(

            # 🔹 Título categoría
            rx.heading(
                "Categoría: " + PublicState.nombre_categoria_actual,
                size="6",
            ),

            rx.divider(),
            rx.link("← Volver", href="/articulos"),

            # 🔹 Listado de posts
            rx.foreach(
                PublicState.posts_categoria,
                lambda post: rx.box(
                    rx.vstack(
                        rx.heading(post.titulo, size="4"),
                        rx.text(post.contenido[:120] + "..."),
                        rx.link(
                            "Leer más",
                            href=f"/articulo/{post.slug}",
                        ),
                        spacing="2",
                        align="start",
                    ),
                    padding="1em",
                    border="1px solid #eee",
                    border_radius="8px",
                    width="100%",
                )
            ),

            

            spacing="4",
            align="start",
            width="100%",
        ),
        padding="2em",
    )