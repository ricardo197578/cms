import reflex as rx
from editorial_cms.states.auth_state import AuthState
from editorial_cms.states.site_config_state import SiteConfigState
from editorial_cms.components.admin_layout import admin_layout


@rx.page(
    route="/admin/configuracion",
    on_load=[AuthState.check_auth, SiteConfigState.cargar_config]
)
def configuracion():

    contenido = rx.vstack(

        rx.heading("Modifica la Pagina Principal", size="7"),

        rx.card(

            rx.vstack(

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

                rx.text("Título del banner (Hero)", weight="bold"),

                rx.input(
                    value=SiteConfigState.hero_title,
                    on_change=SiteConfigState.set_hero_title,
                    width="100%",
                ),

                rx.text("Subtítulo del banner", weight="bold"),

                rx.input(
                    value=SiteConfigState.hero_subtitle,
                    on_change=SiteConfigState.set_hero_subtitle,
                    width="100%",
                ),

                rx.text("Texto del footer", weight="bold"),

                rx.input(
                    value=SiteConfigState.footer_text,
                    on_change=SiteConfigState.set_footer_text,
                    width="100%",
                ),

                rx.button(
                    "Guardar configuración",
                    color_scheme="green",
                    width="100%",
                    on_click=SiteConfigState.guardar
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

                spacing="4"
            ),

            padding="6",
            width="600px"

        ),

        width="100%",
        align="center",
        spacing="6"
    )

    return admin_layout(contenido)