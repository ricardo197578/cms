import reflex as rx
from editorial_cms.components.admin_layout import AdminLayout
from editorial_cms.states.auth_state import AuthState
from editorial_cms.states.site_config_state import SiteConfigState
from editorial_cms.components.container import content_container


@rx.page(
    route="/admin/configuracion",
    on_load=[AuthState.check_auth, SiteConfigState.cargar_config]
)
def configuracion():

    contenido = rx.vstack(

        rx.flex(
            rx.link(
                rx.hstack(
                    rx.icon("arrow-left"),
                    rx.text("Volver"),
                    spacing="2"
                ),
                href="/admin/dashboard",
                text_decoration="none",
            ),
            rx.spacer(),
            rx.heading("Modifica Pagina Inicio y Articulos", size="7"),
            width="100%",
            align="center",
            margin_bottom="4",
        ),

        # 🔹 CONFIGURACIÓN GENERAL
        rx.card(
            rx.vstack(
                rx.heading("Configuración General", size="5"),
                
                rx.text("Nombre del sitio", weight="bold"),
                rx.input(
                    value=SiteConfigState.site_name,
                    on_change=SiteConfigState.set_site_name,
                    width="100%",
                ),

                rx.text("Subtítulo del sitio", weight="bold"),
                rx.input(
                    value=SiteConfigState.site_tagline,
                    on_change=SiteConfigState.set_site_tagline,
                    width="100%",
                ),

                spacing="3"
            ),
            padding="6",
            width="100%"
        ),

        # 🔹 HERO DEL INDEX
        rx.card(
            rx.vstack(
                rx.heading("Hero de la Página Principal", size="5"),
                
                rx.text("Título del hero", weight="bold"),
                rx.input(
                    value=SiteConfigState.hero_title,
                    on_change=SiteConfigState.set_hero_title,
                    width="100%",
                ),

                rx.text("Subtítulo del hero", weight="bold"),
                rx.input(
                    value=SiteConfigState.hero_subtitle,
                    on_change=SiteConfigState.set_hero_subtitle,
                    width="100%",
                ),

                rx.text("Texto del botón", weight="bold"),
                rx.input(
                    value=SiteConfigState.hero_button_text,
                    on_change=SiteConfigState.set_hero_button_text,
                    width="100%",
                ),

                spacing="3"
            ),
            padding="6",
            width="100%"
        ),

        # 🔹 BANNER DE PÁGINAS
        rx.card(
            rx.vstack(
                rx.heading("Banner de Artículos", size="5"),
                
                rx.text("Título del banner", weight="bold"),
                rx.input(
                    value=SiteConfigState.banner_title,
                    on_change=SiteConfigState.set_banner_title,
                    width="100%",
                ),

                rx.text("Subtítulo del banner", weight="bold"),
                rx.input(
                    value=SiteConfigState.banner_subtitle,
                    on_change=SiteConfigState.set_banner_subtitle,
                    width="100%",
                ),

                spacing="3"
            ),
            padding="6",
            width="100%"
        ),

        # 🔹 FOOTER
        rx.card(
            rx.vstack(
                rx.heading("Pie de Página", size="5"),
                
                rx.text("Texto del footer", weight="bold"),
                rx.input(
                    value=SiteConfigState.footer_text,
                    on_change=SiteConfigState.set_footer_text,
                    width="100%",
                ),

                spacing="3"
            ),
            padding="6",
            width="100%"
        ),

        # 🔹 BOTONES DE ACCIÓN
        rx.flex(
            rx.button(
                "Guardar configuración",
                color_scheme="green",
                on_click=SiteConfigState.guardar,
                width=rx.breakpoints(initial="100%", sm="auto")
            ),

            rx.cond(
                SiteConfigState.mensaje != "",
                rx.hstack(
                    rx.text(
                        SiteConfigState.mensaje,
                        color="green",
                        weight="bold"
                    ),

                    rx.button(
                        "✕",
                        size="2",
                        variant="ghost",
                        color_scheme="gray",
                        on_click=SiteConfigState.limpiar_mensaje
                    ),

                    align="center",
                    spacing="3"
                )
            ),

            spacing="4",
            width="100%",
            flex_wrap="wrap",
        ),

        width="100%",
        spacing="5",
    )

    return AdminLayout(content_container(contenido))
