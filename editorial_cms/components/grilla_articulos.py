import reflex as rx

from editorial_cms.states.public_state import PublicState
from editorial_cms.states.site_config_state import SiteConfigState


def _meta_articulo(post) -> rx.Component:
    return rx.hstack(
        rx.text(
            post["fecha_publicacion"],
            font_size=rx.breakpoints(initial="xs", md="sm"),
            color="#94a3b8",
        ),
        rx.text("•", color="#64748b"),
        rx.link(
            "Leer más",
            href="/articulo/" + post.slug,
            on_click=PublicState.iniciar_carga_post,
            font_size=rx.breakpoints(initial="xs", md="sm"),
            color="#3b82f6",
            _hover={"color": "#60a5fa"},
        ),
        spacing="2",
        align="center",
    )


def _tarjeta_minimalista(post) -> rx.Component:
    return rx.vstack(
            rx.heading(
                post.titulo,
                size=rx.breakpoints(initial="4", md="5"),
                color="#f8fafc",
            ),
            rx.text(
                post.contenido[:170] + "...",
                font_size=rx.breakpoints(initial="sm", md="md"),
                color="#cbd5e1",
            ),
        _meta_articulo(post),
        spacing="2",
        align="start",
        width="100%",
        padding_y="1.1em",
        border_bottom="1px solid #1f2937",
    )


def _tarjeta_blog(post) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.cond(
                post.imagen_destacada,
                rx.image(
                    src=rx.get_upload_url(post.imagen_destacada),
                    width="100%",
                    height=rx.breakpoints(initial="180px", md="260px"),
                    object_fit="cover",
                    border_radius="12px",
                ),
            ),
            rx.heading(
                post.titulo,
                size=rx.breakpoints(initial="4", md="5"),
                color="#f8fafc",
            ),
            rx.text(
                post.contenido[:180] + "...",
                font_size=rx.breakpoints(initial="sm", md="md"),
                color="#cbd5e1",
                line_height="1.65",
            ),
            _meta_articulo(post),
            spacing="3",
            align="start",
            width="100%",
        ),
        padding=rx.breakpoints(initial="1.1em", md="1.4em"),
        border="1px solid #334155",
        border_radius="12px",
        background="#0f172a",
        box_shadow="0 10px 24px rgba(2, 6, 23, 0.35)",
        width="100%",
    )


def _tarjeta_revista(post) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.cond(
                post.imagen_destacada,
                rx.image(
                    src=rx.get_upload_url(post.imagen_destacada),
                    width="100%",
                    height="180px",
                    object_fit="cover",
                    border_radius="10px",
                ),
            ),
            rx.heading(post.titulo, size="4", color="#fef3c7"),
            rx.text(
                post.contenido[:110] + "...",
                font_size="sm",
                color="#fde68a",
                line_height="1.6",
            ),
            _meta_articulo(post),
            spacing="2",
            align="start",
            width="100%",
        ),
        padding="1em",
        border="1px solid #a16207",
        border_radius="12px",
        background="#1f150a",
        box_shadow="0 6px 16px rgba(0, 0, 0, 0.4)",
        width="100%",
        _hover={"transform": "translateY(-2px)"},
        transition="all 0.2s ease",
    )


def _tarjeta_portal(post) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.cond(
                post.imagen_destacada,
                rx.image(
                    src=rx.get_upload_url(post.imagen_destacada),
                    width="100%",
                    height=rx.breakpoints(initial="170px", md="210px"),
                    object_fit="cover",
                    border_radius="8px",
                ),
            ),
            rx.heading(post.titulo, size="4", color="#dbeafe"),
            rx.text(
                post.contenido[:140] + "...",
                font_size="sm",
                color="#bfdbfe",
                line_height="1.6",
            ),
            _meta_articulo(post),
            spacing="2",
            align="start",
            width="100%",
        ),
        padding="1em",
        border="1px solid #1d4ed8",
        border_radius="8px",
        background="#0b1324",
        box_shadow="0 2px 8px rgba(0, 0, 0, 0.35)",
        width="100%",
    )


def grilla_articulos(posts) -> rx.Component:
    return rx.cond(
        (SiteConfigState.layout_publico == "blog") | (SiteConfigState.layout_publico == "clasico"),
        rx.vstack(
            rx.foreach(posts, _tarjeta_blog),
            spacing="4",
            width="100%",
        ),
        rx.cond(
            (SiteConfigState.layout_publico == "revista") | (SiteConfigState.layout_publico == "escenario"),
            rx.grid(
                rx.foreach(posts, _tarjeta_revista),
                columns=rx.breakpoints(initial="1", md="2", lg="3"),
                spacing="4",
                width="100%",
            ),
            rx.cond(
                (SiteConfigState.layout_publico == "portal") | (SiteConfigState.layout_publico == "boletin"),
                rx.grid(
                    rx.foreach(posts, _tarjeta_portal),
                    columns=rx.breakpoints(initial="1", md="2"),
                    spacing="4",
                    width="100%",
                ),
                rx.vstack(
                    rx.foreach(posts, _tarjeta_minimalista),
                    spacing="0",
                    width="100%",
                ),
            ),
        ),
    )
