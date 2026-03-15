import reflex as rx  # Importa Reflex para construir componentes UI.
from editorial_cms.components.admin_header import admin_header  # Importa la cabecera del admin.
from editorial_cms.components.admin_sidebar import admin_sidebar  # Importa la barra lateral del admin.


MOBILE = "MOBILE"  # Constante descriptiva para contexto movil.
TABLET = "TABLET"  # Constante descriptiva para contexto tablet.
DESKTOP = "DESKTOP"  # Constante descriptiva para contexto escritorio.


def AdminLayout(
    content: rx.Component,  # Componente principal que renderiza cada pagina.
    show_sidebar: bool = True,  # Indica si se muestra sidebar + header administrativos.
    content_padding: bool = True,  # Indica si el contenido interno lleva padding.
    background: str | rx.Var = "var(--gray-2)",  # Fondo general del layout.
) -> rx.Component:
    sidebar_component = admin_sidebar() if show_sidebar else rx.box(display="none")  # Sidebar visible solo en admin.
    header_component = admin_header() if show_sidebar else rx.box(display="none")  # Header visible solo en admin.
    body_padding = (
        rx.breakpoints(
            initial="14px",  # Padding base en movil.
            md="18px",  # Padding medio en tablet.
            lg="24px",  # Padding mayor en escritorio.
        )
        if content_padding  # Si esta activado el padding, usa breakpoints.
        else "0"  # Si no, elimina padding del body.
    )

    return rx.box(  # Envoltura externa del layout.
        rx.flex(  # Distribuye sidebar y cuerpo principal.
            sidebar_component,  # Inserta el sidebar o un placeholder oculto.
            rx.box(  # Contenedor del area de contenido.
                rx.vstack(  # Apila header y contenido principal verticalmente.
                    header_component,  # Inserta el header o placeholder oculto.
                    rx.box(  # Caja que envuelve el contenido de la pagina.
                        content,  # Renderiza el contenido recibido por parametro.
                        width="100%",  # Ocupa todo el ancho disponible.
                        padding=body_padding,  # Padding configurable/responsivo.
                    ),
                    width="100%",  # El vstack ocupa ancho completo.
                    spacing="0",  # Sin separacion adicional entre bloques.
                    align="stretch",  # Estira hijos para alinear ancho.
                ),
                width="100%",  # El contenedor del body ocupa todo el ancho.
                flex="1",  # Permite que crezca ocupando espacio restante.
                min_width="0",  # Evita desbordes en layouts flex.
            ),
            direction=rx.breakpoints(  # Define direccion del layout segun pantalla.
                initial="column",  # En movil apila elementos.
                md="column",  # En tablet mantiene apilado.
                lg="row",  # En escritorio muestra sidebar a la izquierda.
            ),
            width="100%",  # El flex principal ocupa todo el ancho.
            min_height="100dvh",  # Altura minima viewport dinamico.
            align="stretch",  # Estira bloques para altura uniforme.
            background=background,  # Aplica fondo configurado al contenedor principal.
        ),
        width="100%",  # Caja externa ocupa todo el ancho.
        background=background,  # Repite fondo para continuidad visual.
        color="var(--gray-12)" if show_sidebar else "#e5e7eb",  # Color de texto segun modo admin/publico.
    )


def admin_layout(content: rx.Component) -> rx.Component:  # Alias en snake_case para compatibilidad.
    return AdminLayout(content)  # Reutiliza la funcion principal del layout.
