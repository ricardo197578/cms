import reflex as rx
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
    return rx.vstack(
        # 🔹 BANNER DEL SITIO
        banner(),
        
        # 🔹 CONTENIDO PRINCIPAL
        rx.container(
            rx.flex(
                # 🔹 COLUMNA DE ARTÍCULOS
                rx.box(
                    rx.vstack(
                        rx.heading("Artículos", size="6"),
                        rx.link("← Volver", href="/"),

                        rx.hstack(
                            rx.input(
                                placeholder="Buscar por título...",
                                value=PublicState.busqueda,
                                on_change=PublicState.set_busqueda,
                                debounce_timeout=400,
                                width="300px",
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
                                font_size="sm",
                                color="gray",
                            ),
                        ),

                        rx.cond(
                            PublicState.posts,
                            rx.vstack(
                                rx.foreach(
                                    PublicState.posts,
                                    lambda post: rx.box(
                                        rx.vstack(
                                            rx.heading(post.titulo, size="4"),
                                            rx.text(
                                                post["fecha_publicacion"],
                                                font_size="sm",
                                                color="gray",
                                            ),
                                            rx.text(post.contenido[:120] + "..."),
                                            rx.link(
                                                "Leer más",
                                                href="/articulo/" + post.slug,
                                            ),
                                            spacing="2",
                                            align="start",
                                        ),
                                        padding="1em",
                                        border="1px solid #eee",
                                        border_radius="8px",
                                        width="100%",
                                    ),
                                ),

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
                    # Responsivo: 100% en móvil, 70% en escritorio
                    width=["100%", "100%", "70%"], 
                    padding_bottom=["2em", "2em", "0px"],
                ),

                # 🔹 SIDEBAR
                rx.box(
                    rx.vstack(
                        rx.divider(display=["block", "block", "none"], margin_y="1em"), # Divisor solo en móvil
                        rx.heading("Recientes", size="4"),
                        rx.foreach(
                            PublicState.recientes,
                            lambda post: rx.link(
                                post.titulo,
                                href="/articulo/" + post.slug,
                                font_size="sm",
                            ),
                        ),
                        rx.divider(),
                        rx.heading("Categorías", size="4"),
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
                    # Responsivo: 100% en móvil, 30% en escritorio
                    width=["100%", "100%", "30%"],
                    padding_left=["0px", "0px", "2em"],
                ),
                wrap="wrap", # Permite que el sidebar baje si no hay espacio
                width="100%",
            ),
            padding_y="2em",
            max_width="1100px",
            background="white",
            border_radius="12px",
        ),

        # 🔹 FOOTER DEL SITIO
        footer(),
        
        width="100%",
        align="center",
        min_height="100vh",
    )
