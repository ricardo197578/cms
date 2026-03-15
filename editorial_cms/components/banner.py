import reflex as rx  # Importa Reflex para construir componentes UI.
from editorial_cms.states.site_config_state import SiteConfigState  # Importa estado global de configuracion.


def banner():  # Construye el banner principal de paginas publicas.

    return rx.box(  # Caja externa del banner.

        rx.center(  # Centra horizontalmente el contenido del banner.
            rx.vstack(  # Apila titulo y subtitulo en vertical.

                rx.heading(  # Muestra el nombre del sitio.
                    SiteConfigState.site_name,  # Texto dinamico del nombre configurado.
                    size=rx.breakpoints(initial="4", md="6"),  # Tamano responsivo del heading.
                ),
                
                rx.heading(  # Titulo principal del banner.
                    SiteConfigState.banner_title,  # Texto dinamico configurado por admin.
                    size=rx.breakpoints(initial="5", md="7"),  # Escala responsiva para movil/escritorio.
                    text_align="center",  # Centra el texto del titulo.
                    line_height="1.3",  # Ajusta altura de linea para mejor lectura.
                ),

                rx.text(  # Subtitulo descriptivo del banner.
                    SiteConfigState.banner_subtitle,  # Texto dinamico de subtitulo.
                    font_size=rx.breakpoints(initial="sm", md="md"),  # Tamano responsivo del subtitulo.
                    text_align="center",  # Centra el texto.
                ),

                spacing=rx.breakpoints(initial="2", md="3"),  # Espacio vertical entre elementos.
                align="center",  # Alinea elementos al centro.
                padding_x=rx.breakpoints(initial="1em", md="2em"),  # Padding horizontal responsivo.
            )
        ),

        background=rx.cond(  # Define el gradiente segun layout seleccionado.
            SiteConfigState.layout_publico == "minimalista",  # Si el layout es minimalista...
            "linear-gradient(90deg,#2563eb,#1e40af)",  # ...usa gradiente azul clasico.
            rx.cond(  # Si no es minimalista, evalua el siguiente layout.
                SiteConfigState.layout_publico == "blog",  # Si layout blog...
                "linear-gradient(90deg,#1f2937,#334155)",  # ...usa tonos oscuros periodisticos.
                rx.cond(  # Si no es blog, evalua revista.
                    SiteConfigState.layout_publico == "revista",  # Si layout revista...
                    "linear-gradient(90deg,#5d3b20,#8a5a2b)",  # ...usa tonos calidos editoriales.
                    rx.cond(  # Si no es revista, evalua portal.
                        SiteConfigState.layout_publico == "portal",  # Si layout portal...
                        "linear-gradient(90deg,#123b8a,#1d4ed8,#1e40af)",  # ...usa azul tecnologico.
                        rx.cond(  # Si no es portal, evalua clasico.
                            SiteConfigState.layout_publico == "clasico",  # Si layout clasico...
                            "linear-gradient(90deg,#374151,#111827)",  # ...usa grises sobrios.
                            rx.cond(  # Si no es clasico, evalua boletin.
                                SiteConfigState.layout_publico == "boletin",  # Si layout boletin...
                                "linear-gradient(90deg,#065f46,#047857)",  # ...usa verdes institucionales.
                                "linear-gradient(90deg,#6d28d9,#4c1d95)",  # En otro caso usa esquema escenario.
                            ),
                        ),
                    ),
                ),
            ),
        ),
        color="white",  # Texto del banner en color claro.
        padding=rx.breakpoints(initial="40px 20px", md="60px 40px"),  # Padding vertical/horizontal responsivo.
        width="100%"  # Banner de ancho completo.
    )
