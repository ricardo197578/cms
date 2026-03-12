import reflex as rx
from editorial_cms.states.auth_state import AuthState
from editorial_cms.states.usuario_state import UsuarioState

@rx.page(
    route="/admin/usuarios",
    on_load=[AuthState.check_auth, UsuarioState.cargar_usuarios]
)
def usuarios():
    return rx.cond(
        AuthState.rol_real == "admin",
        rx.container(
            rx.vstack(
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
                    rx.heading("Gestión de Usuarios", size="8"),
                    width="100%",
                    align="center",
                    margin_bottom="4",
                ),
                
                # Formulario de creación estilizado
                rx.card(
                    rx.vstack(
                        rx.text("Crear Nuevo Usuario", weight="bold", size="4"),
                        rx.flex(
                            rx.input(placeholder="Username", on_change=UsuarioState.set_username, flex="1"),
                            rx.input(placeholder="Email", on_change=UsuarioState.set_email, flex="1"),
                            rx.input(placeholder="Password", type="password", on_change=UsuarioState.set_password, flex="1"),
                            rx.select(
                                ["superadmin", "admin", "editor", "autor"],
                                placeholder="Seleccionar Rol",
                                on_change=UsuarioState.set_rol,
                                width="150px"
                            ),
                            rx.button("Crear", on_click=UsuarioState.crear, color_scheme="blue"),
                            spacing="3",
                            flex_wrap="wrap",
                            width="100%"
                        ),
                        spacing="3",
                        width="100%"
                    ),
                    width="100%",
                    padding="5",
                ),

                # Tabla de usuarios
                rx.table.root(
                    rx.table.header(
                        rx.table.row(
                            rx.table.column_header_cell("Usuario"),
                            rx.table.column_header_cell("Rol"),
                            rx.table.column_header_cell("Estado"),
                            rx.table.column_header_cell("Acciones"),
                        ),
                    ),
                    rx.table.body(
                        rx.foreach(
                            UsuarioState.usuarios,
                            lambda u: rx.table.row(
                                rx.table.cell(u.username),
                                rx.table.cell(rx.badge(u.rol, variant="soft", color_scheme="gray")),
                                rx.table.cell(
                                    rx.cond(
                                        u.activo,
                                        rx.badge("Activo", color_scheme="green"),
                                        rx.badge("Inactivo", color_scheme="red"),
                                    )
                                ),
                                rx.table.cell(
                                    rx.button(
                                        "Eliminar",
                                        color_scheme="red",
                                        variant="soft",
                                        size="1",
                                        on_click=lambda: UsuarioState.eliminar(u.id)
                                    )
                                ),
                            )
                        )
                    ),
                    width="100%",
                    variant="surface",
                    margin_top="4",
                ),
                spacing="5",
                width="100%",
            ),
            size="3",
            padding_y="8",
        ),
        rx.center(
            rx.text("No autorizado", color_scheme="red", size="5", weight="bold"),
            height="100vh"
        )
    )
