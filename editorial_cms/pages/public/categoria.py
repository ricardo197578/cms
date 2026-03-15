import reflex as rx
from editorial_cms.components.admin_layout import AdminLayout
from editorial_cms.components.grilla_articulos import grilla_articulos
from editorial_cms.components.layout_theme import ancho_contenido_publico
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
                color="#f8fafc",
            ),

            rx.divider(border_color="var(--gray-6)"),
            rx.link(
                "← Volver",
                href="/articulos",
                font_size=rx.breakpoints(initial="sm", md="md"),
                color="#3b82f6",
                _hover={"color": "#60a5fa"},
            ),

            # 🔹 Listado de posts
            rx.cond(
                PublicState.posts_categoria,
                grilla_articulos(PublicState.posts_categoria),
                rx.heading("No hay artículos en esta categoría", color="#cbd5e1"),
            ),

            

                spacing="4",
                align="start",
                width="100%",
            ),
            padding="2em",
            max_width=ancho_contenido_publico(),
            background="#070b14",
            border_radius=rx.breakpoints(initial="12px", md="14px"),
            border="1px solid #1e293b",
            box_shadow="0 18px 40px rgba(2, 6, 23, 0.45)",
        ),
        show_sidebar=False,
        content_padding=False,
        background="#020617",
    )
