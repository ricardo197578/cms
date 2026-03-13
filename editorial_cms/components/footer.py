import reflex as rx
from editorial_cms.states.site_config_state import SiteConfigState

def footer():
    return rx.box(
        rx.center(
            rx.vstack(
                rx.text(
                    SiteConfigState.footer_text,
                    font_weight="bold",
                    font_size=rx.breakpoints(initial="sm", md="md"),
                ),
                rx.hstack(
                    rx.link("Facebook", href=SiteConfigState.facebook_url, color="white", font_size=rx.breakpoints(initial="xs", md="sm"), _hover={"color": "#93c5fd"}),
                    rx.link("Twitter", href=SiteConfigState.twitter_url, color="white", font_size=rx.breakpoints(initial="xs", md="sm"), _hover={"color": "#93c5fd"}),
                    rx.link("YouTube", href=SiteConfigState.youtube_url, color="white", font_size=rx.breakpoints(initial="xs", md="sm"), _hover={"color": "#93c5fd"}),
                    rx.link("LinkedIn", href=SiteConfigState.linkedin_url, color="white", font_size=rx.breakpoints(initial="xs", md="sm"), _hover={"color": "#93c5fd"}),
                    spacing=rx.breakpoints(initial="3", md="5"),
                    flex_wrap="wrap",
                ),
                spacing=rx.breakpoints(initial="2", md="3"),
            )
        ),
        background_color="#111827",
        color="#ffffff",
        padding=rx.breakpoints(initial="30px 20px", md="40px"),
        width="100%",
        border_top="4px solid #2563eb",
        text_align="center",
    )
