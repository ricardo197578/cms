import reflex as rx
from editorial_cms.states.site_config_state import SiteConfigState


def banner():

    return rx.box(

        rx.center(
            rx.vstack(

                rx.heading(
                    SiteConfigState.site_name,
                    size=rx.breakpoints(initial="4", md="6"),
                ),
                
                rx.heading(
                    SiteConfigState.banner_title,
                    size=rx.breakpoints(initial="5", md="7"),
                    text_align="center",
                    line_height="1.3",
                ),

                rx.text(
                    SiteConfigState.banner_subtitle,
                    font_size=rx.breakpoints(initial="sm", md="md"),
                    text_align="center",
                ),

                spacing=rx.breakpoints(initial="2", md="3"),
                align="center",
                padding_x=rx.breakpoints(initial="1em", md="2em"),
            )
        ),

        background=rx.cond(
            SiteConfigState.layout_publico == "minimalista",
            "linear-gradient(90deg,#2563eb,#1e40af)",
            rx.cond(
                SiteConfigState.layout_publico == "blog",
                "linear-gradient(90deg,#334155,#475569)",
                rx.cond(
                    SiteConfigState.layout_publico == "revista",
                    "linear-gradient(90deg,#8a5a2b,#c58e4a)",
                    "linear-gradient(90deg,#1d4ed8,#2563eb,#0ea5e9)",
                ),
            ),
        ),
        color="white",
        padding=rx.breakpoints(initial="40px 20px", md="60px 40px"),
        width="100%"
    )
