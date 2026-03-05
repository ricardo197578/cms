import reflex as rx
from editorial_cms.services.post_service import obtener_posts
from editorial_cms.states.public_state import PublicState

@rx.page(route="/articulos")
def articulos():

    posts = obtener_posts()

    if not posts:
        return rx.center(
            rx.heading("No hay artículos publicados")
        )

    return rx.container(
        rx.vstack(
            rx.heading("Artículos"),
            *[
                rx.box(
                    rx.heading(post.titulo),
                    rx.text(post.contenido[:120] + "..."),
                    rx.button(
                        "Leer más",
                        on_click=PublicState.ver_post(post.id),
                        color_scheme="blue"
                    ),
                    rx.divider(),
                    padding="1em",
                    width="100%",
                )

                for post in posts
            ],
            rx.link("← Volver", href="/"),
            spacing="4",
        ),
        padding="2em",
        
    )