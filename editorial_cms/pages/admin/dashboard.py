import reflex as rx
from editorial_cms.states.auth_state import AuthState
from editorial_cms.components.admin_layout import admin_layout


@rx.page(
    route="/admin/dashboard",
    on_load=AuthState.check_auth
)
def dashboard():

    contenido = rx.vstack(
        rx.heading("Panel de Administración"),
        rx.text("Bienvenido al dashboard"),
    )

    return admin_layout(contenido)