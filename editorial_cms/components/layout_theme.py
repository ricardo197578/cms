import reflex as rx  # Base UI reactiva para componer estilos dinamicos en tiempo de ejecucion.
from editorial_cms.states.site_config_state import SiteConfigState  # Estado central que guarda el layout elegido por el usuario.


# Este archivo define "tokens" visuales reutilizables.
# La idea pedagogica es: las paginas no deciden colores/tamanos directo,
# sino que llaman estas funciones y el tema se adapta automaticamente.


# FONDO PRINCIPAL DEL SITIO (con tratamiento especial para movil y desktop).
def fondo_publico() -> rx.Var:
    # En movil usamos colores mas planos para evitar fondos muy brillantes.
    # En desktop permitimos gradientes o variaciones mas ricas.
    return rx.breakpoints(
        # Valor para pantalla inicial (movil).
        initial=rx.cond(
            SiteConfigState.layout_publico == "revista",  # Si el tema es revista...
            "#f4efe6",  # ...fondo marfil suave.
            rx.cond(
                SiteConfigState.layout_publico == "portal",  # Si es portal...
                "#eef3fb",  # ...fondo azul muy claro.
                rx.cond(
                    SiteConfigState.layout_publico == "blog",  # Si es blog...
                    "#f5f1ea",  # ...fondo beige tenue.
                    rx.cond(
                        SiteConfigState.layout_publico == "clasico",  # Si es clasico...
                        "#f3f4f6",  # ...gris claro neutro.
                        rx.cond(
                            SiteConfigState.layout_publico == "boletin",  # Si es boletin...
                            "#edf7f3",  # ...verde claro institucional.
                            rx.cond(
                                SiteConfigState.layout_publico == "escenario",  # Si es escenario...
                                "#f3f0ff",  # ...violeta claro.
                                "var(--gray-1)",  # Fallback final (minimalista u otro valor).
                            ),
                        ),
                    ),
                ),
            ),
        ),
        # Valor para desktop/tablet en adelante.
        md=rx.cond(
            SiteConfigState.layout_publico == "revista",  # Revista en desktop...
            "linear-gradient(180deg, #efe4d2 0%, #f7f1e7 40%, #f9f4ec 100%)",  # ...usa gradiente editorial.
            rx.cond(
                SiteConfigState.layout_publico == "portal",  # Portal en desktop...
                "#eaf1fb",  # ...fondo azul claro plano.
                rx.cond(
                    SiteConfigState.layout_publico == "blog",  # Blog en desktop...
                    "#f2eee8",  # ...fondo beige plano.
                    rx.cond(
                        SiteConfigState.layout_publico == "clasico",  # Clasico en desktop...
                        "#eef0f3",  # ...gris elegante.
                        rx.cond(
                            SiteConfigState.layout_publico == "boletin",  # Boletin en desktop...
                            "linear-gradient(180deg, #e8f5ef 0%, #f4faf7 100%)",  # ...gradiente verde suave.
                            rx.cond(
                                SiteConfigState.layout_publico == "escenario",  # Escenario en desktop...
                                "linear-gradient(180deg, #ede9fe 0%, #f6f3ff 100%)",  # ...gradiente violeta suave.
                                "var(--gray-1)",  # Fallback general.
                            ),
                        ),
                    ),
                ),
            ),
        ),
    )


# ANCHO MAXIMO PARA LA ZONA CENTRAL DE CONTENIDO.
def ancho_contenido_publico() -> rx.Var:
    return rx.cond(
        SiteConfigState.layout_publico == "portal",  # Portal prioriza mas densidad de informacion.
        "1280px",  # Ancho mayor.
        rx.cond(
            SiteConfigState.layout_publico == "revista",  # Revista tambien amplia pero menos que portal.
            "1180px",
            "1100px",  # Resto de temas usan ancho base.
        ),
    )


# BORDE EXTERNO PARA TARJETAS/BLOQUES.
def borde_tarjeta_publica() -> rx.Var:
    return rx.cond(
        SiteConfigState.layout_publico == "minimalista",  # Minimalista usa borde gris del sistema.
        "1px solid var(--gray-6)",
        rx.cond(
            SiteConfigState.layout_publico == "blog",  # Blog usa borde arena.
            "1px solid #e8e4dc",
            rx.cond(
                SiteConfigState.layout_publico == "revista",  # Revista usa borde dorado suave.
                "1px solid #dccfb6",
                rx.cond(
                    SiteConfigState.layout_publico == "portal",  # Portal usa borde azul frio.
                    "1px solid #dbe3f1",
                    rx.cond(
                        SiteConfigState.layout_publico == "clasico",  # Clasico usa gris neutral.
                        "1px solid #d1d5db",
                        rx.cond(
                            SiteConfigState.layout_publico == "boletin",  # Boletin usa verde suave.
                            "1px solid #b6e1cf",
                            "1px solid #d8c8ff",  # Escenario (fallback final) usa violeta claro.
                        ),
                    ),
                ),
            ),
        ),
    )


# SOMBRA PARA TARJETAS (con intensidad diferente en movil vs desktop).
def sombra_tarjeta_publica() -> rx.Var:
    return rx.breakpoints(
        initial="0 2px 6px rgba(0,0,0,0.06)",  # En movil: sombra corta y sutil.
        md=rx.cond(
            SiteConfigState.layout_publico == "minimalista",  # Minimalista: sombra muy leve.
            "0 1px 3px rgba(0, 0, 0, 0.08)",
            rx.cond(
                SiteConfigState.layout_publico == "blog",  # Blog: sombra mas amplia.
                "0 12px 30px rgba(52, 48, 41, 0.08)",
                rx.cond(
                    SiteConfigState.layout_publico == "revista",  # Revista: sombra editorial media.
                    "0 6px 18px rgba(89, 65, 29, 0.14)",
                    rx.cond(
                        SiteConfigState.layout_publico == "portal",  # Portal: sombra fria ligera.
                        "0 2px 8px rgba(30, 64, 175, 0.08)",
                        rx.cond(
                            SiteConfigState.layout_publico == "clasico",  # Clasico: sombra neutra.
                            "0 4px 12px rgba(55, 65, 81, 0.1)",
                            rx.cond(
                                SiteConfigState.layout_publico == "boletin",  # Boletin: tono verde.
                                "0 6px 14px rgba(22, 101, 52, 0.1)",
                                "0 8px 16px rgba(109, 40, 217, 0.1)",  # Escenario: tono violeta.
                            ),
                        ),
                    ),
                ),
            ),
        ),
    )


# RADIO DE ESQUINA PARA TARJETAS Y CONTENEDORES.
def radio_tarjeta_publica() -> rx.Var:
    return rx.cond(
        SiteConfigState.layout_publico == "portal",  # Portal: look mas cuadrado.
        "6px",
        rx.cond(
            SiteConfigState.layout_publico == "revista",  # Revista: esquinas mas redondeadas.
            "14px",
            rx.cond(
                SiteConfigState.layout_publico == "escenario",  # Escenario: redondeo premium.
                "16px",
                "10px",  # Resto de layouts.
            ),
        ),
    )


# COLOR PRIMARIO DE INTERACCION (botones, acentos, links importantes).
def color_primario_publico() -> rx.Var:
    return rx.cond(
        SiteConfigState.layout_publico == "revista",  # Revista => dorado oscuro.
        "#8b6f3d",
        rx.cond(
            SiteConfigState.layout_publico == "portal",  # Portal => azul.
            "#2563eb",
            rx.cond(
                SiteConfigState.layout_publico == "blog",  # Blog => cafe grisaceo.
                "#6b5e4b",
                rx.cond(
                    SiteConfigState.layout_publico == "clasico",  # Clasico => gris sobrio.
                    "#374151",
                    rx.cond(
                        SiteConfigState.layout_publico == "boletin",  # Boletin => verde.
                        "#047857",
                        rx.cond(
                            SiteConfigState.layout_publico == "escenario",  # Escenario => violeta.
                            "#7c3aed",
                            "#444",  # Fallback final.
                        ),
                    ),
                ),
            ),
        ),
    )


# PADDING GENERAL RECOMENDADO PARA BLOQUES PRINCIPALES.
def padding_layout_publico() -> rx.Var:
    return rx.cond(
        SiteConfigState.layout_publico == "portal",  # Portal pide mas aire por densidad.
        "32px",
        rx.cond(
            SiteConfigState.layout_publico == "revista",  # Revista usa padding mayor para respiro visual.
            "36px",
            "28px",  # Resto de layouts.
        ),
    )


# FAMILIA TIPOGRAFICA BASE SEGUN IDENTIDAD DE CADA TEMA.
def fuente_layout_publico() -> rx.Var:
    return rx.cond(
        SiteConfigState.layout_publico == "revista",  # Revista: serif clasica.
        "Georgia, serif",
        rx.cond(
            SiteConfigState.layout_publico == "portal",  # Portal: sans moderna.
            "Inter, sans-serif",
            rx.cond(
                SiteConfigState.layout_publico == "clasico",  # Clasico: serif tradicional.
                "Merriweather, serif",
                rx.cond(
                    SiteConfigState.layout_publico == "boletin",  # Boletin: serif limpia.
                    "Lora, serif",
                    rx.cond(
                        SiteConfigState.layout_publico == "escenario",  # Escenario: sans expresiva.
                        "Poppins, sans-serif",
                        "system-ui, sans-serif",  # Minimalista/fallback.
                    ),
                ),
            ),
        ),
    )


# COLOR DE SUPERFICIES (cards/contenedores encima del fondo).
def superficie_publica() -> rx.Var:
    return rx.cond(
        SiteConfigState.layout_publico == "revista",  # Superficie revista.
        "#fcf5e8",
        rx.cond(
            SiteConfigState.layout_publico == "portal",  # Superficie portal.
            "#f3f7ff",
            rx.cond(
                SiteConfigState.layout_publico == "blog",  # Superficie blog.
                "#f9f6f0",
                rx.cond(
                    SiteConfigState.layout_publico == "clasico",  # Superficie clasica.
                    "#f5f5f5",
                    rx.cond(
                        SiteConfigState.layout_publico == "boletin",  # Superficie boletin.
                        "#edf7f3",
                        rx.cond(
                            SiteConfigState.layout_publico == "escenario",  # Superficie escenario.
                            "#f4efff",
                            "var(--gray-1)",  # Fallback base.
                        ),
                    ),
                ),
            ),
        ),
    )


# COLOR DE TITULOS (h1/h2/h3) para mantener contraste correcto por tema.
def color_titulo_publico() -> rx.Var:
    return rx.cond(
        SiteConfigState.layout_publico == "revista",  # Titulo revista.
        "#2f2416",
        rx.cond(
            SiteConfigState.layout_publico == "portal",  # Titulo portal.
            "#0f172a",
            rx.cond(
                SiteConfigState.layout_publico == "blog",  # Titulo blog.
                "#1f2937",
                rx.cond(
                    SiteConfigState.layout_publico == "clasico",  # Titulo clasico.
                    "#111827",
                    rx.cond(
                        SiteConfigState.layout_publico == "boletin",  # Titulo boletin.
                        "#064e3b",
                        rx.cond(
                            SiteConfigState.layout_publico == "escenario",  # Titulo escenario.
                            "#4c1d95",
                            "var(--gray-12)",  # Fallback base.
                        ),
                    ),
                ),
            ),
        ),
    )


# TRANSICION GLOBAL para animaciones de hover/cambio de tema.
def transicion_layout() -> str:
    return "all 0.25s ease"  # Duracion corta y movimiento suave.
