import reflex as rx
from editorial_cms.states.site_config_state import SiteConfigState
from editorial_cms.components.banner import banner
from editorial_cms.components.footer import footer

@rx.page(
    route="/",
    on_load=SiteConfigState.cargar_config
)
def index():
    return rx.box(
        rx.vstack(
            # HEADER
            rx.center(
                rx.flex(
                    rx.heading(SiteConfigState.site_name, size="5"),
                    rx.spacer(),
                    rx.hstack(
                        rx.link("Artículos", href="/articulos"),
                        rx.link("Admin", href="/admin/login"),
                        spacing="4",
                    ),
                    width="100%",
                    max_width="1100px",
                    padding="1.5em",
                    align="center",
                ),
                width="100%",
                border_bottom="1px solid #e5e7eb",
            ),

            # HERO
            rx.center(
                rx.vstack(
                    rx.heading(
                        SiteConfigState.hero_title,
                        size="8", 
                        text_align="center",
                    ),
                    rx.text(
                        SiteConfigState.hero_subtitle,
                        size="4", # Valor fijo compatible
                        color="gray",
                        text_align="center"
                    ),
                    rx.link(
                        rx.button(
                            SiteConfigState.hero_button_text,
                            color_scheme="blue",
                            size="3"
                        ),
                        href="/articulos"
                    ),
                    spacing="6",
                    align="center",
                    width="100%",
                ),
                flex="1",
                width="100%",
                # Los paddings SÍ aceptan listas para responsividad
                padding_y=["4em", "6em", "8em"],
                padding_x="1em",
            ),
            rx.center(
                rx.text(
                    
                    # 🔹 FOOTER DEL SITIO
                    footer(),                   
                    
                ),
                
                padding="2em",
                width="100%",
            ),

            width="100%",
            min_height="100vh",
            spacing="0",
        ),

            

        

        width="100%",

        
    )

