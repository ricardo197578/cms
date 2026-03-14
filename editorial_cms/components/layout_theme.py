import reflex as rx

from editorial_cms.states.site_config_state import SiteConfigState


def fondo_publico() -> rx.Var:
    return rx.cond(
        SiteConfigState.layout_publico == "revista",
        "linear-gradient(180deg, #f6f1e8 0%, #ffffff 35%)",
        rx.cond(
            SiteConfigState.layout_publico == "portal",
            "#f5f7fb",
            rx.cond(
                SiteConfigState.layout_publico == "blog",
                "#fafaf7",
                "var(--gray-1)",
            ),
        ),
    )


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
                "1px solid #dbe3f1",
            ),
        ),
    )


def sombra_tarjeta_publica() -> rx.Var:
    return rx.cond(
        SiteConfigState.layout_publico == "minimalista",
        "0 1px 3px rgba(0, 0, 0, 0.08)",
        rx.cond(
            SiteConfigState.layout_publico == "blog",
            "0 12px 30px rgba(52, 48, 41, 0.08)",
            rx.cond(
                SiteConfigState.layout_publico == "revista",
                "0 6px 18px rgba(89, 65, 29, 0.14)",
                "0 2px 8px rgba(30, 64, 175, 0.08)",
            ),
        ),
    )


def radio_tarjeta_publica() -> rx.Var:
    return rx.cond(
        SiteConfigState.layout_publico == "portal",
        "6px",
        rx.cond(
            SiteConfigState.layout_publico == "revista",
            "14px",
            "10px",
        ),
    )
