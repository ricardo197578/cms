import reflex as rx
from editorial_cms.states.auth_state import AuthState
from editorial_cms.states.site_config_state import SiteConfigState


def sidebar_item(icon, text, href):

    return rx.link(
        rx.hstack(
            rx.icon(icon, size=18),
            rx.text(text),
            spacing="3",
            align="center"
        ),
        href=href,
        width="100%",
        padding="8px",
        border_radius="6px",
        _hover={
            "background_color": "#e5e7eb"
        }
    )


def admin_sidebar():

    return rx.box(

        rx.vstack(

            # LOGO
            # Actualiza el sidebar nombre del sitio automaticamente
            rx.heading(SiteConfigState.site_name, size="6"),                  

            rx.divider(),

            # MENU PRINCIPAL
            sidebar_item("layout-dashboard", "Dashboard", "/admin/dashboard"),
            sidebar_item("file-text", "Crud Artículos", "/admin/posts"),
            sidebar_item("users", "Crud Usuarios", "/admin/usuarios"),
            sidebar_item("settings", "Editar bienvenida", "/admin/configuracion"),
            sidebar_item("settings","Crud Categorías", "/admin/categorias"),
            
            rx.spacer(),

            rx.divider(),

            # SALIR
            rx.button(
                rx.hstack(
                    rx.icon("log-out", size=18),
                    rx.text("Cerrar sesión"),
                    spacing="2"
                ),
                on_click=AuthState.logout,
                variant="soft",
                color_scheme="red",
                width="100%"
            ),

            spacing="4",
            align="start",
            width="100%",
        ),

        width="240px",
        height="100vh",
        padding="20px",
        border_right="1px solid #e5e7eb",
        background_color="#f9fafb",
    )