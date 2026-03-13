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
        rx.flex(
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

            gap="10px",
            align="center",
            wrap=rx.breakpoints(initial="wrap", md="nowrap"),
            justify=rx.breakpoints(initial="start", md="end"),
        ),

        width="100%",
        padding=rx.breakpoints(initial="10px 14px", md="12px 18px", lg="12px 20px"),
        border_bottom="1px solid var(--gray-6)",
        bg="var(--gray-1)",
        align="center",
        justify="between",
        gap="10px",
    )
