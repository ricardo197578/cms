import reflex as rx


def content_container(*children):
    return rx.container(
        *children,
        max_width="900px",
        width="100%",
        margin="0 auto",
        padding_x=rx.breakpoints(initial="1em", md="1.5em", lg="2em"),
        padding_y=rx.breakpoints(initial="1.5em", md="2em", lg="2.5em"),
    )