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
                "linear-gradient(90deg,#1f2937,#334155)",
                rx.cond(
                    SiteConfigState.layout_publico == "revista",
                    "linear-gradient(90deg,#5d3b20,#8a5a2b)",
                    rx.cond(
                        SiteConfigState.layout_publico == "portal",
                        "linear-gradient(90deg,#123b8a,#1d4ed8,#1e40af)",
                        rx.cond(
                            SiteConfigState.layout_publico == "clasico",
                            "linear-gradient(90deg,#374151,#111827)",
                            rx.cond(
                                SiteConfigState.layout_publico == "boletin",
                                "linear-gradient(90deg,#065f46,#047857)",
                                "linear-gradient(90deg,#6d28d9,#4c1d95)",
                            ),
                        ),
                    ),
                ),
            ),
        ),
        color="white",
        padding=rx.breakpoints(initial="40px 20px", md="60px 40px"),
        width="100%"
    )
