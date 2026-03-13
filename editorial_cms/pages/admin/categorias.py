import reflex as rx
from editorial_cms.components.admin_layout import AdminLayout
from editorial_cms.states.categoria_admin_state import CategoriaAdminState
from editorial_cms.components.container import content_container


@rx.page(
    route="/admin/categorias",
    on_load=CategoriaAdminState.cargar
)
def categorias():

    dialogo = rx.alert_dialog.root(
        rx.alert_dialog.content(

            rx.alert_dialog.title("Confirmar eliminación"),

            rx.vstack(

                rx.text("¿Está seguro que desea eliminar la categoría?"),

                rx.badge(
                    CategoriaAdminState.nombre_categoria_eliminar,
                    color_scheme="red",
                    size="3"
                ),

                rx.text(
                    "Esta acción no se puede deshacer.",
                    size="1",
                    color="#666",
                ),

                rx.hstack(

                    rx.alert_dialog.cancel(
                        rx.button(
                            "Cancelar",
                            variant="outline",
                            color_scheme="gray",
                            on_click=CategoriaAdminState.cancelar_eliminacion,
                        )
                    ),

                    rx.alert_dialog.action(
                        rx.button(
                            "Eliminar",
                            color_scheme="red",
                            on_click=CategoriaAdminState.confirmar_eliminacion,
                        )
                    ),

                    spacing="3",
                    justify="end",
                    width="100%",
                ),

                spacing="4",
            ),
        ),
        open=CategoriaAdminState.mostrar_confirmacion,
    )

    contenido = rx.vstack(

        rx.flex(

            rx.link(
                rx.hstack(
                    rx.icon("arrow-left"),
                    rx.text("Volver"),
                    spacing="2"
                ),
                href="/admin/dashboard",
                text_decoration="none",
            ),

            rx.spacer(),

            rx.heading("Gestión de Categorías", size="7"),

            width="100%",
            align="center",
            margin_bottom="4",
        ),

        rx.card(

            rx.vstack(

                rx.cond(
                    CategoriaAdminState.editando_id,
                    rx.heading("Editar Categoría", size="5"),
                    rx.heading("Nueva Categoría", size="5"),
                ),

                rx.text("Nombre de categoría", weight="bold"),

                rx.input(
                    placeholder="Nombre de categoría...",
                    value=CategoriaAdminState.nombre,
                    on_change=CategoriaAdminState.set_nombre,
                    width="100%",
                ),

                rx.flex(

                    rx.cond(
                        CategoriaAdminState.editando_id,

                        rx.hstack(

                            rx.button(
                                "Actualizar",
                                icon="save",
                                color_scheme="blue",
                                on_click=CategoriaAdminState.actualizar,
                            ),

                            rx.button(
                                "Cancelar",
                                icon="x",
                                variant="outline",
                                color_scheme="gray",
                                on_click=CategoriaAdminState.cancelar_edicion,
                            ),

                            spacing="2",
                            width="100%",
                        ),

                        rx.button(
                            "Crear Categoría",
                            icon="plus",
                            color_scheme="grass",
                            on_click=CategoriaAdminState.crear,
                            width="100%",
                        ),
                    ),

                    width="100%",
                ),

                rx.cond(
                    CategoriaAdminState.mensaje != "",
                    rx.text(
                        CategoriaAdminState.mensaje,
                        color=rx.cond(
                            CategoriaAdminState.mensaje.contains("✓"),
                            "green",
                            "red",
                        ),
                        weight="bold"
                    )
                ),

                spacing="3",
                width="100%",
            ),

            padding="6",
            width="100%"
        ),

        rx.card(

            rx.vstack(

                rx.hstack(

                    rx.heading("Categorías Registradas", size="5"),

                    rx.badge(
                        CategoriaAdminState.categorias.length().to_string(),
                        color_scheme="blue",
                    ),

                    spacing="3",
                    width="100%",
                ),

                rx.cond(

                    CategoriaAdminState.categorias.length() > 0,

                    rx.vstack(

                        rx.foreach(
                            CategoriaAdminState.categorias,

                            lambda cat: rx.hstack(

                                rx.box(
                                    rx.vstack(
                                        rx.text(cat.nombre, weight="bold", size="3"),
                                        rx.text(cat.slug, size="1", color="#666"),
                                        spacing="1",
                                    ),
                                    flex="1",
                                ),

                                rx.hstack(

                                    rx.button(
                                        rx.icon("edit"),
                                        size="1",
                                        color_scheme="blue",
                                        variant="outline",
                                        on_click=CategoriaAdminState.set_editando(cat.id),
                                    ),

                                    rx.button(
                                        rx.icon("trash-2"),
                                        size="1",
                                        color_scheme="red",
                                        variant="outline",
                                        on_click=CategoriaAdminState.preparar_eliminacion(cat.id),
                                    ),

                                    spacing="2",
                                ),

                                padding="3",
                                border_bottom="1px solid #e5e7eb",
                                width="100%",
                                align="center",
                            ),
                        ),

                        width="100%",
                        spacing="0",
                    ),

                    rx.box(
                        rx.text("No hay categorías registradas", color="#999"),
                        padding="6",
                        text_align="center",
                    ),
                ),

                spacing="3",
                width="100%",
            ),

            padding="6",
            width="100%"
        ),

        width="100%",
        spacing="5",
    )

    return AdminLayout(
        content_container(
            rx.vstack(
                contenido,
                dialogo,
                width="100%"
            )
        )
    )
