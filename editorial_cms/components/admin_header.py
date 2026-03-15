import reflex as rx  # Importa Reflex para construir componentes UI.
from editorial_cms.states.auth_state import AuthState  # Importa el estado de autenticacion.


def admin_header():  # Define el componente de cabecera del panel admin.

    return rx.flex(  # Contenedor principal horizontal del header.

        rx.spacer(),  # Empuja el bloque de usuario hacia la derecha.

        # Usuario
        rx.flex(  # Contenedor con datos y acciones del usuario.
            rx.icon("user"),  # Icono de usuario autenticado.

            rx.text(  # Texto que muestra el nombre del usuario actual.
                AuthState.username_actual,  # Toma el username desde el estado.
                weight="bold"  # Resalta el nombre en negrita.
            ),

            rx.badge(  # Badge visual para el rol del usuario.
                AuthState.user_role,  # Muestra el rol actual (admin, superadmin, etc.).
                color_scheme="indigo",  # Usa esquema de color indigo.
                variant="soft"  # Estilo suave del badge.
            ),

            rx.button(  # Boton para cerrar la sesion activa.
                "Cerrar sesión",  # Texto visible del boton.
                size="2",  # Tamano compacto del boton.
                color_scheme="red",  # Color de accion de salida.
                variant="soft",  # Variante suave para no saturar visualmente.
                on_click=AuthState.logout  # Ejecuta logout al hacer click.
            ),

            gap="10px",  # Espaciado horizontal entre elementos del bloque usuario.
            align="center",  # Alinea verticalmente al centro.
            wrap=rx.breakpoints(initial="wrap", md="nowrap"),  # En movil permite salto de linea.
            justify=rx.breakpoints(initial="start", md="end"),  # En movil alinea inicio; en desktop al final.
        ),

        width="100%",  # Header ocupa todo el ancho disponible.
        padding=rx.breakpoints(initial="10px 14px", md="12px 18px", lg="12px 20px"),  # Padding responsivo.
        border_bottom="1px solid var(--gray-6)",  # Borde inferior para separar del contenido.
        bg="var(--gray-1)",  # Fondo claro del encabezado.
        align="center",  # Alinea los hijos verticalmente al centro.
        justify="between",  # Distribuye espacio entre extremos.
        gap="10px",  # Espacio base entre bloques principales.
    )
