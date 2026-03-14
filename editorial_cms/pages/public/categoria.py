import reflex as rx
from editorial_cms.components.admin_layout import AdminLayout
from editorial_cms.components.grilla_articulos import grilla_articulos
from editorial_cms.components.layout_theme import (
    ancho_contenido_publico,
    fondo_publico,
)
from editorial_cms.states.public_state import PublicState
from editorial_cms.states.site_config_state import SiteConfigState


@rx.page(
    route="/categoria/[slug]",
    on_load=[SiteConfigState.cargar_config, PublicState.cargar_posts_por_categoria_slug],
)
def categoria():

    return AdminLayout(
        rx.container(
            rx.vstack(

            # 🔹 Título categoría
            rx.heading(
                "Categoría: " + PublicState.nombre_categoria_actual,
                size=rx.breakpoints(initial="5", md="6"),
                color="var(--gray-12)",
            ),

            rx.divider(border_color="var(--gray-6)"),
            rx.link(
                "← Volver",
                href="/articulos",
                font_size=rx.breakpoints(initial="sm", md="md"),
                color="var(--accent-11)",
                _hover={"opacity": "0.8"},
            ),

            # 🔹 Listado de posts
            rx.cond(
                PublicState.posts_categoria,
                grilla_articulos(PublicState.posts_categoria),
                rx.heading("No hay artículos en esta categoría"),
            ),

            

                spacing="4",
                align="start",
                width="100%",
            ),
            padding="2em",
            max_width=ancho_contenido_publico(),
        ),
        show_sidebar=False,
        content_padding=False,
        background=fondo_publico(),
    )
