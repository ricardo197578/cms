import reflex as rx  # Importa Reflex para construir componentes visuales.
from editorial_cms.states.site_config_state import SiteConfigState  # Importa el estado de configuracion del sitio.

def footer():  # Construye el footer global del sitio publico.
    return rx.box(  # Caja principal del footer.
        rx.center(  # Centra horizontalmente el contenido interno.
            rx.vstack(  # Apila texto legal y redes sociales.
                rx.text(  # Texto principal del footer.
                    SiteConfigState.footer_text,  # Valor configurable desde admin.
                    font_weight="bold",  # Resalta el texto en negrita.
                    font_size=rx.breakpoints(initial="sm", md="md"),  # Tamano responsivo del texto.
                ),
                rx.hstack(  # Contenedor horizontal para enlaces sociales.
                    rx.link("Facebook", href=SiteConfigState.facebook_url, color="white", font_size=rx.breakpoints(initial="xs", md="sm"), _hover={"color": "#93c5fd"}),  # Link de Facebook.
                    rx.link("Twitter", href=SiteConfigState.twitter_url, color="white", font_size=rx.breakpoints(initial="xs", md="sm"), _hover={"color": "#93c5fd"}),  # Link de Twitter/X.
                    rx.link("YouTube", href=SiteConfigState.youtube_url, color="white", font_size=rx.breakpoints(initial="xs", md="sm"), _hover={"color": "#93c5fd"}),  # Link de YouTube.
                    rx.link("LinkedIn", href=SiteConfigState.linkedin_url, color="white", font_size=rx.breakpoints(initial="xs", md="sm"), _hover={"color": "#93c5fd"}),  # Link de LinkedIn.
                    spacing=rx.breakpoints(initial="3", md="5"),  # Espaciado responsivo entre links.
                    flex_wrap="wrap",  # Permite salto de linea en pantallas chicas.
                ),
                spacing=rx.breakpoints(initial="2", md="3"),  # Espaciado vertical entre bloques.
            )
        ),
        background_color=rx.cond(  # Define fondo segun layout activo.
            SiteConfigState.layout_publico == "minimalista",  # Si es minimalista...
            "#111827",  # ...fondo azul/gris oscuro.
            rx.cond(  # Si no, evalua blog.
                SiteConfigState.layout_publico == "blog",  # Si es blog...
                "#292524",  # ...fondo pizarra oscuro.
                rx.cond(  # Si no, evalua revista.
                    SiteConfigState.layout_publico == "revista",  # Si es revista...
                    "#3f2d1a",  # ...fondo marron editorial.
                    rx.cond(  # Si no, evalua portal.
                        SiteConfigState.layout_publico == "portal",  # Si es portal...
                        "#0f172a",  # ...fondo azul noche.
                        rx.cond(  # Si no, evalua clasico.
                            SiteConfigState.layout_publico == "clasico",  # Si es clasico...
                            "#1f2937",  # ...fondo gris carbon.
                            rx.cond(  # Si no, evalua boletin.
                                SiteConfigState.layout_publico == "boletin",  # Si es boletin...
                                "#064e3b",  # ...fondo verde institucional.
                                "#312e81",  # Caso restante: escenario violeta oscuro.
                            ),
                        ),
                    ),
                ),
            ),
        ),
        color="#ffffff",  # Color de texto general del footer.
        padding=rx.breakpoints(initial="30px 20px", md="40px"),  # Padding responsivo.
        width="100%",  # Footer de ancho completo.
        border_top=rx.cond(  # Borde superior segun layout activo.
            SiteConfigState.layout_publico == "minimalista",  # Si es minimalista...
            "4px solid #2563eb",  # ...borde azul.
            rx.cond(  # Si no, evalua blog.
                SiteConfigState.layout_publico == "blog",  # Si es blog...
                "4px solid #64748b",  # ...borde gris azulado.
                rx.cond(  # Si no, evalua revista.
                    SiteConfigState.layout_publico == "revista",  # Si es revista...
                    "4px solid #c58e4a",  # ...borde dorado.
                    rx.cond(  # Si no, evalua portal.
                        SiteConfigState.layout_publico == "portal",  # Si es portal...
                        "4px solid #0ea5e9",  # ...borde celeste.
                        rx.cond(  # Si no, evalua clasico.
                            SiteConfigState.layout_publico == "clasico",  # Si es clasico...
                            "4px solid #9ca3af",  # ...borde gris.
                            rx.cond(  # Si no, evalua boletin.
                                SiteConfigState.layout_publico == "boletin",  # Si es boletin...
                                "4px solid #34d399",  # ...borde verde suave.
                                "4px solid #a78bfa",  # Caso restante: borde violeta.
                            ),
                        ),
                    ),
                ),
            ),
        ),
        text_align="center",  # Centra el texto del footer.
    )
