import reflex as rx
from editorial_cms.states.auth_state import AuthState
from editorial_cms.components.admin_layout import admin_layout


@rx.page(
    route="/admin/dashboard",
    on_load=[AuthState.check_auth]
)
def dashboard():

    contenido = rx.vstack(

        rx.heading("Panel de Administración"),

        rx.cond(
            AuthState.user_role == "admin",
            rx.vstack(
                rx.text("Bienvenido Administrador"),
                rx.text("Aquí puedes gestionar usuarios y contenido."),
                spacing="2"
            ),
            rx.vstack(
                rx.text("Bienvenido Editor"),
                rx.text("Puedes crear y editar artículos."),
                spacing="2"
            )
        )

    )

    return admin_layout(contenido)