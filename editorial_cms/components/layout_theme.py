import reflex as rx
from editorial_cms.states.site_config_state import SiteConfigState


# 🔹 FONDO DEL SITIO (RESPONSIVE PARA EVITAR BRILLO EN MÓVIL)
def fondo_publico() -> rx.Var:

    return rx.breakpoints(

        # 📱 MOBILE (más neutro, menos brillo)
        initial=rx.cond(
            SiteConfigState.layout_publico == "revista",
            "#f4efe6",
            rx.cond(
                SiteConfigState.layout_publico == "portal",
                "#eef3fb",
                rx.cond(
                    SiteConfigState.layout_publico == "blog",
                    "#f5f1ea",
                    rx.cond(
                        SiteConfigState.layout_publico == "clasico",
                        "#f3f4f6",
                        rx.cond(
                            SiteConfigState.layout_publico == "boletin",
                            "#edf7f3",
                            rx.cond(
                                SiteConfigState.layout_publico == "escenario",
                                "#f3f0ff",
                                "var(--gray-1)",
                            ),
                        ),
                    ),
                ),
            ),
        ),

        # 💻 DESKTOP (mantiene tu diseño original)
        md=rx.cond(
            SiteConfigState.layout_publico == "revista",
            "linear-gradient(180deg, #efe4d2 0%, #f7f1e7 40%, #f9f4ec 100%)",
            rx.cond(
                SiteConfigState.layout_publico == "portal",
                "#eaf1fb",
                rx.cond(
                    SiteConfigState.layout_publico == "blog",
                    "#f2eee8",
                    rx.cond(
                        SiteConfigState.layout_publico == "clasico",
                        "#eef0f3",
                        rx.cond(
                            SiteConfigState.layout_publico == "boletin",
                            "linear-gradient(180deg, #e8f5ef 0%, #f4faf7 100%)",
                            rx.cond(
                                SiteConfigState.layout_publico == "escenario",
                                "linear-gradient(180deg, #ede9fe 0%, #f6f3ff 100%)",
                                "var(--gray-1)",
                            ),
                        ),
                    ),
                ),
            ),
        ),
    )


# 🔹 ANCHO MÁXIMO DEL CONTENIDO
def ancho_contenido_publico() -> rx.Var:
    return rx.cond(
        SiteConfigState.layout_publico == "portal",
        "1280px",
        rx.cond(
            SiteConfigState.layout_publico == "revista",
            "1180px",
            "1100px",
        ),
    )


# 🔹 BORDE DE TARJETAS
def borde_tarjeta_publica() -> rx.Var:
    return rx.cond(
        SiteConfigState.layout_publico == "minimalista",
        "1px solid var(--gray-6)",
        rx.cond(
            SiteConfigState.layout_publico == "blog",
            "1px solid #e8e4dc",
            rx.cond(
                SiteConfigState.layout_publico == "revista",
                "1px solid #dccfb6",
                rx.cond(
                    SiteConfigState.layout_publico == "portal",
                    "1px solid #dbe3f1",
                    rx.cond(
                        SiteConfigState.layout_publico == "clasico",
                        "1px solid #d1d5db",
                        rx.cond(
                            SiteConfigState.layout_publico == "boletin",
                            "1px solid #b6e1cf",
                            "1px solid #d8c8ff",
                        ),
                    ),
                ),
            ),
        ),
    )


# 🔹 SOMBRA DE TARJETAS (RESPONSIVE)
def sombra_tarjeta_publica() -> rx.Var:

    return rx.breakpoints(

        # 📱 móvil (sombras suaves)
        initial="0 2px 6px rgba(0,0,0,0.06)",

        # 💻 desktop
        md=rx.cond(
            SiteConfigState.layout_publico == "minimalista",
            "0 1px 3px rgba(0, 0, 0, 0.08)",
            rx.cond(
                SiteConfigState.layout_publico == "blog",
                "0 12px 30px rgba(52, 48, 41, 0.08)",
                rx.cond(
                    SiteConfigState.layout_publico == "revista",
                    "0 6px 18px rgba(89, 65, 29, 0.14)",
                    rx.cond(
                        SiteConfigState.layout_publico == "portal",
                        "0 2px 8px rgba(30, 64, 175, 0.08)",
                        rx.cond(
                            SiteConfigState.layout_publico == "clasico",
                            "0 4px 12px rgba(55, 65, 81, 0.1)",
                            rx.cond(
                                SiteConfigState.layout_publico == "boletin",
                                "0 6px 14px rgba(22, 101, 52, 0.1)",
                                "0 8px 16px rgba(109, 40, 217, 0.1)",
                            ),
                        ),
                    ),
                ),
            ),
        ),
    )


# 🔹 RADIO DE TARJETAS
def radio_tarjeta_publica() -> rx.Var:
    return rx.cond(
        SiteConfigState.layout_publico == "portal",
        "6px",
        rx.cond(
            SiteConfigState.layout_publico == "revista",
            "14px",
            rx.cond(
                SiteConfigState.layout_publico == "escenario",
                "16px",
                "10px",
            ),
        ),
    )


# 🔹 COLOR PRINCIPAL DEL SITIO
def color_primario_publico() -> rx.Var:
    return rx.cond(
        SiteConfigState.layout_publico == "revista",
        "#8b6f3d",
        rx.cond(
            SiteConfigState.layout_publico == "portal",
            "#2563eb",
            rx.cond(
                SiteConfigState.layout_publico == "blog",
                "#6b5e4b",
                rx.cond(
                    SiteConfigState.layout_publico == "clasico",
                    "#374151",
                    rx.cond(
                        SiteConfigState.layout_publico == "boletin",
                        "#047857",
                        rx.cond(
                            SiteConfigState.layout_publico == "escenario",
                            "#7c3aed",
                            "#444",
                        ),
                    ),
                ),
            ),
        ),
    )


# 🔹 PADDING GENERAL DEL LAYOUT
def padding_layout_publico() -> rx.Var:
    return rx.cond(
        SiteConfigState.layout_publico == "portal",
        "32px",
        rx.cond(
            SiteConfigState.layout_publico == "revista",
            "36px",
            "28px",
        ),
    )


# 🔹 TIPOGRAFÍA DEL SITIO
def fuente_layout_publico() -> rx.Var:
    return rx.cond(
        SiteConfigState.layout_publico == "revista",
        "Georgia, serif",
        rx.cond(
            SiteConfigState.layout_publico == "portal",
            "Inter, sans-serif",
            rx.cond(
                SiteConfigState.layout_publico == "clasico",
                "Merriweather, serif",
                rx.cond(
                    SiteConfigState.layout_publico == "boletin",
                    "Lora, serif",
                    rx.cond(
                        SiteConfigState.layout_publico == "escenario",
                        "Poppins, sans-serif",
                        "system-ui, sans-serif",
                    ),
                ),
            ),
        ),
    )


# 🔹 COLOR DE SUPERFICIE (CONTENEDORES)
def superficie_publica() -> rx.Var:
    return rx.cond(
        SiteConfigState.layout_publico == "revista",
        "#fcf5e8",
        rx.cond(
            SiteConfigState.layout_publico == "portal",
            "#f3f7ff",
            rx.cond(
                SiteConfigState.layout_publico == "blog",
                "#f9f6f0",
                rx.cond(
                    SiteConfigState.layout_publico == "clasico",
                    "#f5f5f5",
                    rx.cond(
                        SiteConfigState.layout_publico == "boletin",
                        "#edf7f3",
                        rx.cond(
                            SiteConfigState.layout_publico == "escenario",
                            "#f4efff",
                            "var(--gray-1)",
                        ),
                    ),
                ),
            ),
        ),
    )


# 🔹 COLOR DE TÍTULOS
def color_titulo_publico() -> rx.Var:
    return rx.cond(
        SiteConfigState.layout_publico == "revista",
        "#2f2416",
        rx.cond(
            SiteConfigState.layout_publico == "portal",
            "#0f172a",
            rx.cond(
                SiteConfigState.layout_publico == "blog",
                "#1f2937",
                rx.cond(
                    SiteConfigState.layout_publico == "clasico",
                    "#111827",
                    rx.cond(
                        SiteConfigState.layout_publico == "boletin",
                        "#064e3b",
                        rx.cond(
                            SiteConfigState.layout_publico == "escenario",
                            "#4c1d95",
                            "var(--gray-12)",
                        ),
                    ),
                ),
            ),
        ),
    )


# 🔹 TRANSICIÓN GENERAL PARA ELEMENTOS
def transicion_layout() -> str:
    return "all 0.25s ease"
