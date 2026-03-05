import reflex as rx
from editorial_cms.states.auth_state import AuthState


@rx.page(route="/admin/login")
def login():
    return rx.center(
        rx.vstack(
            rx.heading("Login Administrador"),
            rx.link("← Volver", href="/"),
            rx.input(
                placeholder="Usuario",
                on_change=AuthState.set_username
            ),
            rx.input(
                placeholder="Contraseña",
                type="password",
                on_change=AuthState.set_password
            ),
            rx.button(
                "Ingresar",
                on_click=AuthState.login
            ),
            rx.text(AuthState.error, color="red"),
            spacing="4",
        ),
        
        height="100vh",
    )