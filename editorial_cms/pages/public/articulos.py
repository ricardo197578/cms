import reflex as rx
from editorial_cms.states.public_state import PublicState


@rx.page(
    route="/articulos",
    # Carga solo los publicados
    on_load=PublicState.cargar_publicados
)
def articulos():

    return rx.container(
        rx.vstack(
            rx.heading("Artículos"),

            rx.cond(
                PublicState.posts,

                # 🔹 Si hay artículos
                rx.foreach(
                    PublicState.posts,
                    lambda post: rx.box(
                        rx.heading(post.titulo),
                        rx.text(post.contenido[:120] + "..."),
                        rx.link(
                            "Leer más",
                            href="/articulo/"+ post.slug,
                            color="blue"
                        ),
                        rx.divider(),
                        padding="1em",
                        width="100%",
                    )
                ),

                # 🔹 Si NO hay artículos
                rx.center(
                    rx.heading("No hay artículos publicados")
                ),
            ),

            rx.link("← Volver", href="/"),
            spacing="4",
        ),
        padding="2em",
    )