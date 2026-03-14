import reflex as rx
from editorial_cms.components.admin_layout import AdminLayout
from editorial_cms.components.grilla_articulos import grilla_articulos
from editorial_cms.components.layout_theme import (
    ancho_contenido_publico,
    borde_tarjeta_publica,
    fondo_publico,
    radio_tarjeta_publica,
)
from editorial_cms.states.public_state import PublicState
from editorial_cms.states.site_config_state import SiteConfigState
from editorial_cms.components.banner import banner
from editorial_cms.components.footer import footer


@rx.page(
    route="/articulos",
    on_load=[
        SiteConfigState.cargar_config,
        PublicState.resetear_paginacion,
        PublicState.cargar_categorias_sidebar,
        PublicState.cargar_recientes,
    ],
)
def articulos():
    return AdminLayout(
        rx.vstack(
        # 🔹 BANNER DEL SITIO
        banner(),
        
        # 🔹 CONTENIDO PRINCIPAL
        rx.container(
            rx.flex(
                # 🔹 COLUMNA DE ARTÍCULOS
                rx.box(
                    rx.vstack(
                        rx.heading(
                            "Artículos", 
                            size=rx.breakpoints(initial="5", md="6"),
                            color="var(--gray-12)"
                        ),
                        rx.link(
                            "← Volver",
                            href="/",
                            font_size=rx.breakpoints(initial="sm", md="md"),
                            color="var(--accent-11)",
                            _hover={"opacity": "0.8"},
                        ),

                        rx.hstack(
                            rx.input(
                                placeholder="Buscar por título...",
                                value=PublicState.busqueda,
                                on_change=PublicState.set_busqueda,
                                debounce_timeout=400,
                                width=rx.breakpoints(initial="100%", md="300px"),
                                font_size=rx.breakpoints(initial="sm", md="md"),
                                padding=rx.breakpoints(initial="8px", md="10px"),
                            ),
                            rx.cond(
                                PublicState.mostrando_resultados,
                                rx.button(
                                    "✕",
                                    size="2",
                                    on_click=PublicState.limpiar_busqueda,
                                ),
                            ),
                        ),

                        rx.cond(
                            PublicState.mostrando_resultados,
                            rx.text(
                                "Resultados para: " + PublicState.busqueda,
                                font_size=rx.breakpoints(initial="xs", md="sm"),
                                color="var(--gray-10)",
                                margin_top="0.5em",
                            ),
                        ),

                        rx.cond(
                            PublicState.posts,
                            rx.vstack(
                                grilla_articulos(PublicState.posts),

                                rx.hstack(
                                    rx.button(
                                        "← Anterior",
                                        on_click=PublicState.pagina_anterior,
                                        is_disabled=~PublicState.puede_ir_atras,
                                    ),
                                    rx.text("Página " + PublicState.page.to_string()),
                                    rx.button(
                                        "Siguiente →",
                                        on_click=PublicState.siguiente_pagina,
                                        is_disabled=~PublicState.puede_ir_adelante,
                                    ),
                                    spacing="4",
                                ),
                            ),
                            rx.heading("No hay artículos publicados"),
                        ),
                        spacing="4",
                        align="start",
                        width="100%",
                    ),
                    # Responsivo: 100% en móvil, 68% en desktop
                    width=rx.breakpoints(initial="100%", md="68%"),
                    padding_bottom=rx.breakpoints(initial="1.5em", md="2em", lg="0px"),
                    padding_x=rx.breakpoints(initial="1em", md="0"),
                    spacing=rx.breakpoints(initial="3", md="4"),
                ),

                # 🔹 SIDEBAR
                rx.box(
                    rx.vstack(
                        rx.divider(display=rx.breakpoints(initial="block", md="block", lg="none"), margin_y="1em"),
                        rx.heading(
                            "Recientes",
                            size=rx.breakpoints(initial="4", md="5"),
                            color="var(--gray-12)",
                        ),
                        rx.foreach(
                            PublicState.recientes,
                            lambda post: rx.link(
                                post.titulo,
                                href="/articulo/" + post.slug,
                                on_click=PublicState.iniciar_carga_post,
                                font_size=rx.breakpoints(initial="sm", md="md"),
                                color="var(--accent-11)",
                                _hover={"color": "var(--accent-12)", "text_decoration": "underline"},
                                display="block",
                                padding_y="0.5em",
                            ),
                        ),
                        rx.divider(margin_y="1.5em"),
                        rx.heading(
                            "Categorías",
                            size=rx.breakpoints(initial="4", md="5"),
                            color="var(--gray-12)",
                        ),
                        rx.cond(
                            PublicState.hay_categoria_activa,
                            rx.button(
                                "Limpiar filtro",
                                size="2",
                                variant="outline",
                                on_click=PublicState.set_categoria(""),
                            ),
                        ),
                        rx.foreach(
                            PublicState.categorias_sidebar,
                            lambda cat: rx.hstack(
                                rx.button(
                                    cat.nombre,
                                    variant=rx.cond(
                                        PublicState.categoria_activa == cat.slug,
                                        "solid",
                                        "ghost"
                                    ),
                                    color_scheme=rx.cond(
                                        PublicState.categoria_activa == cat.slug,
                                        "blue",
                                        "gray"
                                    ),
                                    on_click=PublicState.set_categoria(cat.slug),
                                ),
                                rx.spacer(),
                                rx.badge(cat.cantidad),
                                width="100%",
                            ),
                        ),
                        spacing="3",
                        align="start",
                    ),
                    # Responsivo: 100% en móvil, 32% en desktop
                    width=rx.breakpoints(initial="100%", md="32%"),
                    padding_left=rx.breakpoints(initial="1em", md="1.2em", lg="2em"),
                    spacing=rx.breakpoints(initial="2", md="3"),
                ),
                direction=rx.breakpoints(initial="column", md="row"),
                align="start",
                width="100%",
                gap=rx.breakpoints(initial="1em", md="2em"),
            ),
            padding=rx.breakpoints(initial="1.5em", md="2em"),
            max_width=ancho_contenido_publico(),
            background=rx.cond(
                SiteConfigState.layout_publico == "minimalista",
                "var(--gray-1)",
                "#ffffff",
            ),
            border_radius=radio_tarjeta_publica(),
            border=rx.cond(
                SiteConfigState.layout_publico == "minimalista",
                "none",
                borde_tarjeta_publica(),
            ),
            box_shadow=rx.cond(
                SiteConfigState.layout_publico == "minimalista",
                "0 1px 3px rgba(0, 0, 0, 0.05)",
                "0 18px 40px rgba(15, 23, 42, 0.06)",
            ),
        ),

        # 🔹 FOOTER DEL SITIO
        footer(),
        
        width="100%",
        align="center",
        min_height="100vh",
        ),
        show_sidebar=False,
        content_padding=False,
        background=fondo_publico(),
    )
