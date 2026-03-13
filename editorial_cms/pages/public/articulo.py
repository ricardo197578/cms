import reflex as rx
from editorial_cms.components.admin_layout import AdminLayout
from editorial_cms.states.public_state import PublicState
from editorial_cms.components.container import content_container


@rx.page(
    route="/articulo/[slug]",
    on_load=PublicState.cargar_por_slug,
)
def articulo():

    return AdminLayout(
        rx.cond(
            PublicState.post_actual,

            content_container(

                rx.vstack(

                # 🔹 BREADCRUMB
                rx.flex(
                    rx.link(
                        rx.hstack(
                            rx.icon("arrow-left", size=18),
                            rx.text(
                                "Volver",
                                font_size=rx.breakpoints(initial="sm", md="md"),
                            ),
                            spacing="2"
                        ),
                        href="/articulos",
                        text_decoration="none",
                        color="var(--accent-11)",
                        _hover={"color": "var(--accent-12)", "opacity": "0.8"},
                    ),

                    rx.spacer(),

                    rx.hstack(
                        rx.link(
                            "Inicio",
                            href="/",
                            color="var(--gray-10)",
                            underline="none",
                            font_size=rx.breakpoints(initial="xs", md="sm"),
                            _hover={"color": "var(--gray-12)"},
                        ),
                        rx.text("/", color="var(--gray-9)", font_size=rx.breakpoints(initial="xs", md="sm")),

                        rx.cond(
                            PublicState.post_actual.categoria,
                            rx.link(
                                PublicState.post_actual.categoria.nombre,
                                href="/categoria/" + PublicState.post_actual.categoria.slug,
                                color="var(--accent-11)",
                                underline="none",
                                font_size=rx.breakpoints(initial="xs", md="sm"),
                                _hover={"color": "var(--accent-12)"},
                            ),
                        ),

                        spacing="2",
                        align="center",
                    ),

                    width="100%",
                    align="center",
                    padding_bottom=rx.breakpoints(initial="1em", md="1.5em"),
                    padding_x=rx.breakpoints(initial="0.5em", md="0"),
                    border_bottom="1px solid var(--gray-6)",
                    margin_bottom=rx.breakpoints(initial="1.5em", md="2em"),
                    flex_wrap="wrap",
                ),

                # 🔹 CABECERA
                rx.vstack(

                    rx.cond(
                        PublicState.post_actual.categoria,
                        rx.link(
                            rx.badge(
                                PublicState.post_actual.categoria.nombre,
                                variant="soft",
                                color_scheme="blue",
                                size="2",
                            ),
                            href="/categoria/" + PublicState.post_actual.categoria.slug,
                            _hover={"opacity": "0.8"},
                        ),
                    ),

                    rx.heading(
                        PublicState.post_actual.titulo,
                        size=rx.breakpoints(initial="5", md="8"),
                        weight="bold",
                        color="var(--gray-12)",
                        line_height="1.3",
                    ),

                    rx.hstack(
                        rx.icon(
                            "calendar",
                            size=16,
                            color="var(--gray-10)",
                        ),
                        rx.text(
                            PublicState.post_actual.fecha_publicacion,
                            size="2",
                            color="var(--gray-10)",
                        ),
                        rx.text("•", color="var(--gray-9)"),
                        rx.icon(
                            "clock",
                            size=16,
                            color="var(--gray-10)",
                        ),
                        rx.text(
                            "5 min de lectura",
                            size="2",
                            color="var(--gray-10)",
                        ),
                        spacing="2",
                        align="center",
                        flex_wrap="wrap",
                    ),

                    spacing=rx.breakpoints(initial="2", md="3"),
                    width="100%",
                ),

                rx.divider(),

                # 🔹 CONTENIDO
                rx.box(
                    rx.markdown(
                        PublicState.post_actual.contenido,
                    ),
                    width="100%",
                    style={
                        "font-size": "clamp(0.95rem, 2vw, 1.1rem)",
                        "line-height": "1.9",
                        "color": "var(--gray-12)",
                        "word-break": "break-word",
                    },
                ),

                spacing=rx.breakpoints(initial="4", md="6"),
                width="100%",
                align="start",
                )
            ),

            # 🔹 ERROR
            rx.center(
                rx.vstack(
                    rx.heading("Artículo no encontrado", size="6"),
                    rx.link(
                        rx.button("Regresar a Artículos", color_scheme="blue"),
                        href="/articulos",
                    ),
                    spacing="4",
                ),
                width="100%",
                height="100vh",
            ),
        ),
        show_sidebar=False,
        content_padding=False,
        background="var(--gray-1)",
    )
