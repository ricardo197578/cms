import reflex as rx
from editorial_cms.components.admin_header import admin_header
from editorial_cms.components.admin_sidebar import admin_sidebar


def admin_layout(content: rx.Component) -> rx.Component:

    return rx.hstack(

        admin_sidebar(),

        rx.vstack(

            admin_header(),            

            rx.box(
                content,
                padding="25px",
                width="100%"
            ),

            width="100%",
            spacing="0",
        ),

        width="100%",
        align="start",
    )