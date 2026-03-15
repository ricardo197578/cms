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
        background_color=rx.cond(
            SiteConfigState.layout_publico == "minimalista",
            "#111827",
            rx.cond(
                SiteConfigState.layout_publico == "blog",
                "#292524",
                rx.cond(
                    SiteConfigState.layout_publico == "revista",
                    "#3f2d1a",
                    rx.cond(
                        SiteConfigState.layout_publico == "portal",
                        "#0f172a",
                        rx.cond(
                            SiteConfigState.layout_publico == "clasico",
                            "#1f2937",
                            rx.cond(
                                SiteConfigState.layout_publico == "boletin",
                                "#064e3b",
                                "#312e81",
                            ),
                        ),
                    ),
                ),
            ),
        ),
        color="#ffffff",
        padding=rx.breakpoints(initial="30px 20px", md="40px"),
        width="100%",
        border_top=rx.cond(
            SiteConfigState.layout_publico == "minimalista",
            "4px solid #2563eb",
            rx.cond(
                SiteConfigState.layout_publico == "blog",
                "4px solid #64748b",
                rx.cond(
                    SiteConfigState.layout_publico == "revista",
                    "4px solid #c58e4a",
                    rx.cond(
                        SiteConfigState.layout_publico == "portal",
                        "4px solid #0ea5e9",
                        rx.cond(
                            SiteConfigState.layout_publico == "clasico",
                            "4px solid #9ca3af",
                            rx.cond(
                                SiteConfigState.layout_publico == "boletin",
                                "4px solid #34d399",
                                "4px solid #a78bfa",
                            ),
                        ),
                    ),
                ),
            ),
        ),
        text_align="center",
    )
