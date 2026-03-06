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
                rx.heading(PublicState.post_actual.titulo),
                rx.text(PublicState.post_actual.contenido),
                rx.link("← Volver", href="/articulos"),
                spacing="4",
            ),
            padding="2em",
        ),
        rx.center(
            rx.heading("Artículo no encontrado")
        )
    )