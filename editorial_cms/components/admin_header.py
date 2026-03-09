import reflex as rx
from editorial_cms.states.auth_state import AuthState


def admin_header():

    return rx.flex(

        # Buscador
        # rx.input(
         #    placeholder="Buscar artículos...",
          #   width="300px",
         #    size="3"
        # ),

        rx.spacer(),

        # Usuario
        rx.hstack(
            rx.icon("user"),

            rx.text(
                AuthState.usuario_logueado["username"],
                weight="bold"
            ),

            rx.badge(
                AuthState.usuario_logueado["rol"],
                color_scheme="indigo",
                variant="soft"
            ),

            rx.button(
                "Cerrar sesión",
                size="2",
                color_scheme="red",
                variant="soft",
                on_click=AuthState.logout
            ),

            spacing="3",
            align="center"
        ),

        width="100%",
        padding="12px",
        border_bottom="1px solid #e5e7eb",
        bg="white",
        align="center"
    )