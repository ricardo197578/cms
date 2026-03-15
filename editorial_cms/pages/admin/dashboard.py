import reflex as rx
from editorial_cms.states.auth_state import AuthState
from editorial_cms.states.site_config_state import SiteConfigState
from editorial_cms.components.admin_layout import AdminLayout

@rx.page(
    route="/admin/dashboard",
    on_load=[AuthState.check_auth, SiteConfigState.cargar_config]
)
def dashboard():
    # Estilizamos el contenido interno
    contenido = rx.vstack(
        # Cabecera con saludo dinámico
        rx.flex(
            rx.vstack(
                rx.heading(
                    "¡Hola, " + AuthState.username_actual + "!",
                    size="8"
                ),
                rx.text("Bienvenido al panel de control de Editorial CMS", color_scheme="gray"),
                align_items="start",
            ),
            rx.spacer(),
            rx.badge(
                rx.icon("user", size=16),
                AuthState.user_role,
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

        rx.card(
            rx.vstack(
                rx.hstack(
                    rx.icon("layout-panel-top"),
                    rx.heading("Layout público", size="4"),
                    spacing="2",
                    align="center",
                ),
                rx.text(
                    "Elegi el estilo visual del sitio y guarda para aplicarlo.",
                    color_scheme="gray",
                    size="2",
                ),
                rx.hstack(
                    rx.select(
                        [
                            "minimalista",
                            "blog",
                            "revista",
                            "portal",
                            "clasico",
                            "boletin",
                            "escenario",
                        ],
                        value=SiteConfigState.layout_publico,
                        on_change=SiteConfigState.set_layout_publico,
                        width=rx.breakpoints(initial="100%", md="260px"),
                    ),
                    rx.button(
                        "Guardar layout",
                        color_scheme="blue",
                        on_click=SiteConfigState.guardar,
                    ),
                    spacing="3",
                    width="100%",
                    flex_wrap="wrap",
                ),
                rx.cond(
                    SiteConfigState.mensaje != "",
                    rx.text(SiteConfigState.mensaje, color="green", weight="medium", size="2"),
                ),
                spacing="3",
                align="start",
            ),
            width="100%",
            margin_top="2",
            variant="surface",
        ),
        
        spacing="4",
        width="100%",
        align_items="stretch",
    )

    return AdminLayout(contenido)
