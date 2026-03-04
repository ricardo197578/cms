import reflex as rx

@rx.page(route="/")
def index():
    return rx.center(
        rx.vstack(
            rx.heading("Bienvenido al sitio"),
            rx.text("Este contenido es público."),
            rx.link("Ir a Artículos", href="/articulos"),
            rx.link("Login Admin", href="/admin/login"),
            spacing="4"
        ),
        padding="5em"
    )