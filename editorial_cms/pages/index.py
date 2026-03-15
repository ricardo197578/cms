import reflex as rx  # Importa la librería principal de Reflex
from editorial_cms.components.admin_layout import AdminLayout
from editorial_cms.states.site_config_state import SiteConfigState  # Importa el estado que maneja la configuración del sitio
from editorial_cms.components.footer import footer  # Importa el componente footer para el pie de página

@rx.page(  # Decorador que define una página en Reflex
    route="/",  # Define la ruta principal del sitio (página de inicio)
    on_load=SiteConfigState.cargar_config  # Función que se ejecuta al cargar la página para obtener la configuración
)
def index():  # Función que define el contenido de la página principal
    return AdminLayout(
        rx.box(  # Contenedor principal de la página (div)
        rx.vstack(  # Organiza los elementos verticalmente (stack vertical)
            # HEADER  # Comentario: sección del encabezado
            rx.center(  # Centra el contenido horizontalmente
                rx.flex(  # Contenedor flexible para organizar elementos en fila
                    rx.vstack(  # Organiza verticalmente el nombre y tagline
                        rx.heading(
                            SiteConfigState.site_name,
                            size="5",
                            color="#f8fafc",
                        ),  # Muestra el nombre del sitio como título, tamaño 5
                        rx.text(SiteConfigState.site_tagline, size="2", color="#cbd5e1"),  # Muestra el subtítulo/tagline del sitio
                        spacing="1"  # Poco espacio entre el nombre y el tagline
                    ),
                    rx.spacer(),  # Espaciador que empuja los elementos siguientes a la derecha
                    rx.hstack(  # Organiza los enlaces horizontalmente
                        rx.link("Artículos", href="/articulos", color="#93c5fd"),  # Enlace a la página de artículos
                        rx.link("Admin", href="/admin/login", color="#93c5fd"),  # Enlace al panel de administración
                        spacing="4",  # Espacio entre los elementos del hstack
                    ),
                    width="100%",  # Ancho completo del flex
                    max_width="1100px",  # Ancho máximo de 1100 píxeles
                    padding="1.5em",  # Relleno interno de 1.5em
                    align="center",  # Alinea los elementos al centro verticalmente
                ),
                width="100%",  # Ancho completo del contenedor center
                border_bottom=rx.cond(
                    SiteConfigState.layout_publico == "revista",
                    "1px solid #dccfb6",
                    "1px solid #e5e7eb",
                ),
            ),

            # HERO  # Comentario: sección principal o hero
            rx.center(  # Centra el contenido horizontalmente
                rx.box(
                    rx.vstack(  # Organiza los elementos verticalmente
                        rx.heading(  # Título principal
                            SiteConfigState.hero_title,  # Título obtenido del estado
                            size=rx.cond(
                                SiteConfigState.layout_publico == "portal",
                                "7",
                                "8",
                            ),
                            color="#f8fafc",
                            text_align="center",  # Texto centrado
                        ),
                        rx.text(  # Subtítulo
                            SiteConfigState.hero_subtitle,  # Subtítulo obtenido del estado
                            size="4",  # Tamaño fijo compatible
                            color="#cbd5e1",  # Color de texto gris
                            text_align="center"  # Texto centrado
                        ),
                        rx.link(  # Enlace para el botón
                            rx.button(  # Botón
                                SiteConfigState.hero_button_text,  # Texto del botón obtenido del estado
                                color_scheme=rx.cond(
                                    SiteConfigState.layout_publico == "revista",
                                    "amber",
                                    rx.cond(
                                        SiteConfigState.layout_publico == "portal",
                                        "indigo",
                                        "blue",
                                    ),
                                ),
                                size="3"  # Tamaño del botón
                            ),
                            href="/articulos"  # Enlace a la página de artículos
                        ),
                        spacing="6",  # Espacio entre elementos del vstack
                        align="center",  # Alinea los elementos al centro
                        width="100%",  # Ancho completo
                    ),
                    width="100%",
                    max_width="920px",
                    padding=rx.cond(
                        SiteConfigState.layout_publico == "minimalista",
                        "0",
                        rx.cond(
                            SiteConfigState.layout_publico == "portal",
                            "1.8em",
                            "2.4em",
                        ),
                    ),
                    background="#070b14",
                    border="1px solid #1e293b",
                    border_radius=rx.cond(
                        SiteConfigState.layout_publico == "portal",
                        "8px",
                        "16px",
                    ),
                    box_shadow="0 18px 40px rgba(2, 6, 23, 0.45)",
                ),
                flex="1",  # El contenedor puede crecer para ocupar espacio disponible
                width="100%",  # Ancho completo
                # Los paddings SÍ aceptan listas para responsividad
                padding_y=["4em", "6em", "8em"],  # Padding vertical responsivo: móvil, tablet, escritorio
                padding_x="1em",  # Padding horizontal fijo
            ),
            
            # 🔹 FOOTER DEL SITIO  # Comentario: sección del pie de página
            footer(),  # Renderiza el componente footer importado

            width="100%",  # Ancho completo del vstack principal
            min_height="100vh",  # Altura mínima del viewport completo
            spacing="0",  # Sin espacio entre elementos del vstack
        ),

        width="100%",  # Ancho completo del box principal

        ),
        show_sidebar=False,
        content_padding=False,
        background="#020617",
    )
