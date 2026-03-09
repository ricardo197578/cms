import reflex as rx
from editorial_cms.states.site_config_state import SiteConfigState


def footer():

    return rx.box(

        rx.center(

            rx.vstack(

                rx.text(SiteConfigState.footer_text),

                rx.hstack(

                    rx.link("Facebook", href=SiteConfigState.facebook_url),
                    rx.link("Twitter", href=SiteConfigState.twitter_url),
                    rx.link("YouTube", href=SiteConfigState.youtube_url),
                    rx.link("LinkedIn", href=SiteConfigState.linkedin_url),

                    spacing="5"
                ),

                spacing="3"
            )
        ),

        padding="40px",
        border_top="1px solid #e5e7eb",
        margin_top="60px"
    )