import reflex as rx
from editorial_cms.states.public_state import PublicState
from editorial_cms.components.container import content_container


@rx.page(
    route="/articulo/[slug]",
    on_load=PublicState.cargar_por_slug,
)
def articulo():

    return rx.cond(
        PublicState.post_actual,

        content_container(

            rx.vstack(

                # 🔹 BREADCRUMB
                rx.flex(
                    rx.link(
                        rx.hstack(
                            rx.icon("arrow-left", size=18),
                            rx.text("Volver"),
                            spacing="2"
                        ),
                        href="/articulos",
                        text_decoration="none",
                        _hover={"opacity": "0.8"},
                    ),

                    rx.spacer(),

                    rx.hstack(
                        rx.link("Inicio", href="/", color_scheme="gray", underline="none"),
                        rx.text("/", color_scheme="gray"),

                        rx.cond(
                            PublicState.post_actual.categoria,
                            rx.link(
                                PublicState.post_actual.categoria.nombre,
                                href="/categoria/" + PublicState.post_actual.categoria.slug,
                                color_scheme="gray",
                                underline="none",
                            ),
                        ),

                        spacing="2",
                        font_size="12px",
                        align="center",
                    ),

                    width="100%",
                    align="center",
                    padding_bottom="1em",
                    border_bottom="1px solid #e5e7eb",
                    margin_bottom="2em",
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
                        ),
                    ),

                    rx.heading(
                        PublicState.post_actual.titulo,
                        size=rx.breakpoints(initial="6", md="8"),
                        weight="bold",
                    ),

                    rx.hstack(
                        rx.icon("calendar", size=16),
                        rx.text(
                            PublicState.post_actual.fecha_publicacion,
                            size="2",
                            color="gray"
                        ),
                        rx.text("•", color="gray"),
                        rx.icon("clock", size=16),
                        rx.text("5 min de lectura", size="2", color="gray"),
                        spacing="2",
                        align="center",
                    ),

                    spacing="3",
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
                        "font-size": "1.05rem",
                        "line-height": "1.9",
                        "color": "var(--gray-11)",
                        "word-break": "break-word",
                    },
                ),

                spacing="6",
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
    )