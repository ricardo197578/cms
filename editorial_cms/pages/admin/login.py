import reflex as rx
from editorial_cms.states.auth_state import AuthState


@rx.page(route="/admin/login")
def login():
    return rx.center(

        rx.box(

            rx.vstack(

                rx.heading(
                    "Login Administrador",
                    size=rx.breakpoints(initial="5", md="7"),
                    text_align="center",
                    color="var(--gray-12)",
                ),

                rx.link(
                    "← Volver",
                    href="/",
                    font_size=rx.breakpoints(initial="xs", md="sm"),
                    color="var(--accent-11)",
                ),

                rx.input(
                    placeholder="Usuario",
                    on_change=AuthState.set_username,
                    width="100%",
                    font_size=rx.breakpoints(initial="sm", md="md"),
                    color="var(--gray-12)",
                    background="var(--gray-1)",
                    border="1px solid var(--gray-7)",
                    _placeholder={"color": "var(--gray-10)"},
                ),

                rx.input(
                    placeholder="Contraseña",
                    type="password",
                    on_change=AuthState.set_password,
                    width="100%",
                    font_size=rx.breakpoints(initial="sm", md="md"),
                    color="var(--gray-12)",
                    background="var(--gray-1)",
                    border="1px solid var(--gray-7)",
                    _placeholder={"color": "var(--gray-10)"},
                ),

                rx.button(
                    "Ingresar",
                    on_click=AuthState.login,
                    width="100%",
                    size=rx.breakpoints(initial="2", md="3"),
                ),

                rx.text(
                    AuthState.error,
                    color="red",
                    text_align="center",
                    font_size=rx.breakpoints(initial="xs", md="sm"),
                ),

                spacing="4",
                width="100%",
            ),

            width="100%",
            max_width="420px",
            padding=rx.breakpoints(initial="20px", md="32px"),
            border_radius="12px",
            box_shadow="lg",
            border="1px solid var(--gray-6)",
            background="var(--gray-2)",
        ),

        height="100vh",
        background="var(--gray-3)",
        padding=rx.breakpoints(initial="12px", md="16px"),
    )
