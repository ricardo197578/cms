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
        width=rx.breakpoints(initial="auto", lg="100%"),
        padding=rx.breakpoints(initial="7px 10px", lg="8px"),
        border_radius="8px",
        color="var(--gray-12)",
        background="transparent",
        border="1px solid transparent",
        _hover={
            "background_color": "var(--gray-3)",
            "border_color": "var(--gray-6)",
            "text_decoration": "none",
        },
        _focus_visible={
            "outline": "2px solid var(--accent-8)",
            "outline_offset": "2px",
        },
        text_decoration="none",
    )


def admin_sidebar():

    return rx.box(

        rx.vstack(

            # LOGO
            # Actualiza el sidebar nombre del sitio automaticamente
            rx.heading(
                SiteConfigState.site_name,
                size=rx.breakpoints(initial="4", md="5", lg="6"),
                color="var(--gray-12)",
            ),

            rx.divider(),

            # MENU PRINCIPAL
            rx.flex(
                sidebar_item("layout-dashboard", "Dashboard", "/admin/dashboard"),
                sidebar_item("file-text", "Crud Artículos", "/admin/posts"),
                sidebar_item("users", "Crud Usuarios", "/admin/usuarios"),
                sidebar_item("settings", "Editar bienvenida", "/admin/configuracion"),
                sidebar_item("settings", "Crud Categorías", "/admin/categorias"),
                direction=rx.breakpoints(initial="row", lg="column"),
                wrap=rx.breakpoints(initial="wrap", lg="nowrap"),
                gap="8px",
                width="100%",
            ),

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
                width=rx.breakpoints(initial="100%", lg="100%")
            ),

            spacing="4",
            align="start",
            width="100%",
        ),

        width=rx.breakpoints(initial="100%", md="100%", lg="260px"),
        height=rx.breakpoints(initial="auto", lg="100dvh"),
        min_width=rx.breakpoints(initial="auto", lg="260px"),
        padding=rx.breakpoints(initial="14px", md="16px", lg="20px"),
        border_right=rx.breakpoints(initial="none", lg="1px solid var(--gray-6)"),
        border_bottom=rx.breakpoints(initial="1px solid var(--gray-6)", lg="none"),
        background_color="var(--gray-2)",
        position=rx.breakpoints(initial="static", lg="sticky"),
        top=rx.breakpoints(initial="auto", lg="0"),
        z_index="10",
    )
