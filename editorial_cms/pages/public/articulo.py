import reflex as rx
from editorial_cms.states.public_state import PublicState


@rx.page(route="/articulo")
def articulo():

    return rx.container(
        rx.cond(
            PublicState.post_actual,

            rx.vstack(
                rx.heading(PublicState.post_actual.titulo),
                rx.text(PublicState.post_actual.contenido),
                rx.link("← Volver", href="/articulos"),
                spacing="4"
            ),

            rx.center(
                rx.heading("Artículo no seleccionado")
            )
        ),
        padding="2em",
    )