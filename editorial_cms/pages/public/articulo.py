import reflex as rx
from editorial_cms.states.public_state import PublicState


@rx.page(
    route="/articulo/[slug]",
    on_load=PublicState.cargar_por_slug,
)
def articulo():

    return rx.cond(
        PublicState.post_actual,
        rx.container(
            rx.vstack(

                # 🔹 BREADCRUMB
                rx.hstack(
                    rx.link("Inicio", href="/"),
                    rx.text(">"),
                    rx.cond(
                        PublicState.post_actual.categoria,
                        rx.link(
                            PublicState.post_actual.categoria.nombre,
                            href="/categoria/" + PublicState.post_actual.categoria.slug,
                        ),
                    ),
                    rx.text(">"),
                    rx.text(
                        PublicState.post_actual.titulo,
                        font_weight="bold",
                    ),
                    spacing="2",
                    font_size="sm",
                    color="gray",
                ),

                rx.divider(),
                rx.link("← Volver", href="/articulos"),
                # 🔹 TÍTULO
                rx.heading(
                    PublicState.post_actual.titulo,
                    size="6",
                ),

                # 🔹 BADGE CATEGORÍA
                rx.cond(
                    PublicState.post_actual.categoria,
                    rx.link(
                        rx.badge(
                            PublicState.post_actual.categoria.nombre,
                            color_scheme="blue",
                        ),
                        href="/categoria/" + PublicState.post_actual.categoria.slug,
                    ),
                ),

                rx.divider(),

                # 🔹 CONTENIDO
                rx.text(
                    PublicState.post_actual.contenido,
                    font_size="md",
                ),

                

                spacing="4",
                align="start",
            ),
            padding="2em",
            max_width="800px",
        ),
        rx.center(
            rx.heading("Artículo no encontrado")
        )
    )