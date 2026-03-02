import reflex as rx
from editorial_cms.states.auth_state import AuthState


@rx.page(
    route="/admin/dashboard",
    on_load=AuthState.check_auth
)
def dashboard():

    return rx.vstack(
        rx.heading("Panel de Administración"),
        rx.text("Bienvenido al dashboard"),
        rx.text(AuthState.username_actual),
        rx.button("Cerrar sesión", on_click=AuthState.logout),
        spacing="4",
        padding="6"
    )