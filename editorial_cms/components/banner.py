import reflex as rx
from editorial_cms.states.site_config_state import SiteConfigState


def banner():

    return rx.box(

        rx.center(
            rx.vstack(

                rx.heading(SiteConfigState.site_name, size="6"),   
                
                rx.heading(                   
                    SiteConfigState.banner_title,
                    size="7"
                ),

                rx.text(
                    SiteConfigState.banner_subtitle,
                    color="gray"
                ),

                spacing="3",
                align="center"
            )
        ),

        background="linear-gradient(90deg,#2563eb,#1e40af)",
        color="white",
        padding="60px",
        width="100%"
    )