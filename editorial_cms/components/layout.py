import reflex as rx
from editorial_cms.components.footer import footer

def layout(*children):
    return rx.box(
        rx.vstack(
            *children,
            footer(),
            width="100%",
            min_height="100vh",
            spacing="0",
        ),
        width="100%",
        background="var(--gray-1)",
    )