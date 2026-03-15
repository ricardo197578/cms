import reflex as rx  # Importa Reflex para construir UI.
from editorial_cms.states.auth_state import AuthState  # Estado de autenticacion del usuario.
from editorial_cms.states.site_config_state import SiteConfigState  # Estado de configuracion del sitio.


def sidebar_item(icon, text, href):  # Componente reutilizable para cada opcion del menu.

    return rx.link(  # Link completo clickeable para navegar en el panel.
        rx.hstack(  # Agrupa icono y texto del item.
            rx.icon(icon, size=18),  # Icono configurable del item.
            rx.text(text),  # Texto visible del item.
            spacing="3",  # Espaciado entre icono y texto.
            align="center"  # Alineacion vertical centrada.
        ),
        href=href,  # Ruta de destino del item.
        width=rx.breakpoints(initial="auto", lg="100%"),  # En desktop ocupa toda la fila.
        padding=rx.breakpoints(initial="7px 10px", lg="8px"),  # Padding responsivo del item.
        border_radius="8px",  # Bordes redondeados del link.
        color="var(--gray-12)",  # Color base del texto/icono.
        background="transparent",  # Fondo transparente por defecto.
        border="1px solid transparent",  # Borde transparente para evitar saltos al hover.
        _hover={  # Estilos de hover para mejor feedback visual.
            "background_color": "var(--gray-3)",  # Fondo suave al pasar el mouse.
            "border_color": "var(--gray-6)",  # Borde visible al hover.
            "text_decoration": "none",  # Evita subrayado del enlace.
        },
        _focus_visible={  # Estilos para accesibilidad con teclado.
            "outline": "2px solid var(--accent-8)",  # Contorno visible en foco.
            "outline_offset": "2px",  # Separacion del contorno.
        },
        text_decoration="none",  # Sin subrayado en estado normal.
    )


def admin_sidebar():  # Construye el sidebar completo del admin.

    return rx.box(  # Caja principal del sidebar.

        rx.vstack(  # Organiza todo el contenido del sidebar en vertical.

            # LOGO
            # Actualiza el sidebar nombre del sitio automaticamente
            rx.heading(  # Titulo/logo del sitio en el sidebar.
                SiteConfigState.site_name,  # Nombre dinamico del sitio.
                size=rx.breakpoints(initial="4", md="5", lg="6"),  # Tamano responsivo del titulo.
                color="var(--gray-12)",  # Color del titulo.
            ),

            rx.divider(),  # Separador visual debajo del logo.

            # MENU PRINCIPAL
            rx.flex(  # Contenedor de items del menu.
                sidebar_item("layout-dashboard", "Dashboard", "/admin/dashboard"),  # Acceso a dashboard.
                sidebar_item("file-text", "Crud Artículos", "/admin/posts"),  # Acceso a gestion de articulos.
                sidebar_item("users", "Crud Usuarios", "/admin/usuarios"),  # Acceso a gestion de usuarios.
                sidebar_item("settings", "Editar bienvenida", "/admin/configuracion"),  # Acceso a config de bienvenida.
                sidebar_item("settings", "Crud Categorías", "/admin/categorias"),  # Acceso a gestion de categorias.
                direction=rx.breakpoints(initial="row", lg="column"),  # En movil en fila, en desktop en columna.
                wrap=rx.breakpoints(initial="wrap", lg="nowrap"),  # Permite salto en movil.
                gap="8px",  # Espaciado entre items.
                width="100%",  # Ancho completo del bloque menu.
            ),

            rx.spacer(),  # Empuja el bloque de salida hacia el final.

            rx.divider(),  # Separador superior del boton salir.

            # SALIR
            rx.button(  # Boton de cierre de sesion.
                rx.hstack(  # Contenido interno del boton salir.
                    rx.icon("log-out", size=18),  # Icono de salida.
                    rx.text("Cerrar sesión"),  # Texto del boton.
                    spacing="2"  # Espacio entre icono y texto.
                ),
                on_click=AuthState.logout,  # Evento para cerrar sesion.
                variant="soft",  # Variante suave del boton.
                color_scheme="red",  # Esquema rojo para accion destructiva.
                width=rx.breakpoints(initial="100%", lg="100%")  # Ocupa todo el ancho siempre.
            ),

            spacing="4",  # Espacio entre bloques internos del sidebar.
            align="start",  # Alinea elementos al inicio.
            width="100%",  # VStack interno ocupa ancho completo.
        ),

        width=rx.breakpoints(initial="100%", md="100%", lg="260px"),  # Ancho total en movil, fijo en desktop.
        height=rx.breakpoints(initial="auto", lg="100dvh"),  # Alto auto en movil, full viewport en desktop.
        min_width=rx.breakpoints(initial="auto", lg="260px"),  # Evita que colapse en desktop.
        padding=rx.breakpoints(initial="14px", md="16px", lg="20px"),  # Padding responsivo.
        border_right=rx.breakpoints(initial="none", lg="1px solid var(--gray-6)"),  # Borde lateral en desktop.
        border_bottom=rx.breakpoints(initial="1px solid var(--gray-6)", lg="none"),  # Borde inferior en movil.
        background_color="var(--gray-2)",  # Fondo del sidebar.
        position=rx.breakpoints(initial="static", lg="sticky"),  # Sticky solo en desktop.
        top=rx.breakpoints(initial="auto", lg="0"),  # Fija el sidebar al top en desktop.
        z_index="10",  # Prioridad de capa para superposiciones.
    )
