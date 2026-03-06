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

                # TÍTULO
                rx.heading(
                    PublicState.post_actual.titulo
                ),

                # CATEGORÍA (Badge clickeable)
                rx.cond(
                    PublicState.post_actual.categoria,
                    rx.link(
                        rx.badge(
                            PublicState.post_actual.categoria.nombre,
                            color_scheme="blue",
                            variant="soft",
                        ),
                        href="/categoria/" + PublicState.post_actual.categoria.slug,
                    ),
                ),

                rx.divider(),

                # CONTENIDO
                rx.text(
                    PublicState.post_actual.contenido
                ),

                # VOLVER
                rx.link(
                    "← Volver",
                    href="/articulos"
                ),

                spacing="4",
            ),
            padding="2em",
        ),

        # SI NO EXISTE
        rx.center(
            rx.heading("Artículo no encontrado")
        )
    )