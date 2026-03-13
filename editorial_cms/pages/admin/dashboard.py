import reflex as rx
from editorial_cms.states.auth_state import AuthState
from editorial_cms.components.admin_layout import AdminLayout

@rx.page(
    route="/admin/dashboard",
    on_load=[AuthState.check_auth]
)
def dashboard():
    # Estilizamos el contenido interno
    contenido = rx.vstack(
        # Cabecera con saludo dinámico
        rx.flex(
            rx.vstack(
                rx.heading(
                    f"¡Hola, {AuthState.usuario_logueado['username']}!", 
                    size="8"
                ),
                rx.text("Bienvenido al panel de control de Editorial CMS", color_scheme="gray"),
                align_items="start",
            ),
            rx.spacer(),
            rx.badge(
                rx.icon("user", size=16),
                AuthState.usuario_logueado["rol"],
                size="3", 
                color_scheme="indigo", 
                variant="soft",
                padding_x="3"
            ),
            width="100%",
            align="center",
            padding_bottom="6",
        ),

        # Grid de Tarjetas de Acceso Rápido / Estadísticas
        rx.grid(
            rx.card(
                rx.vstack(
                    rx.icon("files", size=30, color=rx.color("indigo", 9)),
                    rx.text("Artículos", weight="bold"),
                    rx.text("Gestioná tus publicaciones", size="2"),
                    align_items="center",
                ),
                padding="4",
            ),
            rx.card(
                rx.vstack(
                    rx.icon("message-square", size=30, color=rx.color("grass", 9)),
                    rx.text("Comentarios", weight="bold"),
                    rx.text("Moderá la interacción", size="2"),
                    align_items="center",
                ),
                padding="4",
            ),
            # Esta tarjeta solo destaca si es superadmin
            rx.cond(
                AuthState.user_role == "superadmin",
                rx.card(
                    rx.vstack(
                        rx.icon("users", size=30, color=rx.color("tomato", 9)),
                        rx.text("Usuarios", weight="bold"),
                        rx.text("Control de permisos", size="2"),
                        align_items="center",
                    ),
                    padding="4",
                ),
            ),
            columns=rx.breakpoints(initial="1", sm="3"),
            spacing="4",
            width="100%",
        ),

        # Sección de mensajes específicos por rol (Tu lógica original mejorada)
        rx.card(
            rx.cond(
                AuthState.user_role == "superadmin",
                rx.vstack(
                    rx.hstack(
                        rx.icon("shield-check", color="green"),
                        rx.text("Acceso Total Habilitado", weight="bold", size="4"),
                    ),
                    rx.text("Tenés permisos para gestionar usuarios, roles y la configuración global del sistema."),
                    spacing="3",
                ),
                rx.vstack(
                    rx.hstack(
                        rx.icon("pen-tool", color="blue"),
                        rx.text("Modo Editor", weight="bold", size="4"),
                    ),
                    rx.text("Tu flujo de trabajo está listo: podés crear, editar y organizar los artículos del portal."),
                    spacing="3",
                )
            ),
            width="100%",
            margin_top="6",
            variant="surface",
        ),
        
        spacing="4",
        width="100%",
        align_items="stretch",
    )

    return AdminLayout(contenido)
