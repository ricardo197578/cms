import reflex as rx
from editorial_cms.states.auth_state import AuthState


def admin_layout(content: rx.Component) -> rx.Component:
    return rx.vstack(

        # HEADER
        rx.hstack(
            rx.text(f"Usuario: {AuthState.usuario_logueado['username']}"),
            rx.spacer(),
            rx.button(
                "Cerrar sesión",
                on_click=AuthState.logout
            ),
            width="100%",
            padding="10px",
            border_bottom="1px solid #ddd",
        ),

        # CUERPO
        rx.hstack(

            # SIDEBAR
            rx.vstack(
                rx.link("Dashboard", href="/admin/dashboard"),
                rx.link("Artículos", href="/admin/posts"),
                spacing="4",
                width="200px",
                padding="10px",
                border_right="1px solid #ddd",
                height="100vh"
            ),

            # CONTENIDO DINÁMICO
            rx.box(
                content,
                padding="20px",
                width="100%"
            ),

            width="100%",
        ),

        width="100%",
    )