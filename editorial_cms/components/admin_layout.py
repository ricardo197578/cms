import reflex as rx
from editorial_cms.components.admin_header import admin_header
from editorial_cms.components.admin_sidebar import admin_sidebar


MOBILE = "MOBILE"
TABLET = "TABLET"
DESKTOP = "DESKTOP"


def AdminLayout(
    content: rx.Component,
    show_sidebar: bool = True,
    content_padding: bool = True,
    background: str | rx.Var = "var(--gray-2)",
) -> rx.Component:
    sidebar_component = admin_sidebar() if show_sidebar else rx.box(display="none")
    header_component = admin_header() if show_sidebar else rx.box(display="none")
    body_padding = (
        rx.breakpoints(
            initial="14px",
            md="18px",
            lg="24px",
        )
        if content_padding
        else "0"
    )

    return rx.box(
        rx.flex(
            sidebar_component,
            rx.box(
                rx.vstack(
                    header_component,
                    rx.box(
                        content,
                        width="100%",
                        padding=body_padding,
                    ),
                    width="100%",
                    spacing="0",
                    align="stretch",
                ),
                width="100%",
                flex="1",
                min_width="0",
            ),
            direction=rx.breakpoints(
                initial="column",
                md="column",
                lg="row",
            ),
            width="100%",
            min_height="100dvh",
            align="stretch",
            background=background,
        ),
        width="100%",
        background=background,
        color="var(--gray-12)" if show_sidebar else "#e5e7eb",
    )


def admin_layout(content: rx.Component) -> rx.Component:
    return AdminLayout(content)
