import reflex as rx
from editorial_cms.states.site_config_state import SiteConfigState

def footer():
    return rx.box(
        rx.center(
            rx.vstack(
                rx.text(
                    SiteConfigState.footer_text,
                    font_weight="bold", # Un toque extra de estilo
                ),
                rx.hstack(
                    rx.link("Facebook", href=SiteConfigState.facebook_url, color="white", _hover={"color": "#2563eb"}),
                    rx.link("Twitter", href=SiteConfigState.twitter_url, color="white", _hover={"color": "#2563eb"}),
                    rx.link("YouTube", href=SiteConfigState.youtube_url, color="white", _hover={"color": "#2563eb"}),
                    rx.link("LinkedIn", href=SiteConfigState.linkedin_url, color="white", _hover={"color": "#2563eb"}),
                    spacing="5",
                ),
                spacing="3",
            )
        ),
        # Estilos aplicados correctamente en Reflex:
        background_color="#111827",  # Gris oscuro moderno
        color="#ffffff",             # Texto blanco
        padding_top="40px",          # Espaciado superior
        padding_bottom="40px",       # Espaciado inferior
        width="100%",                # Para que ocupe todo el ancho
        border_top="4px solid #2563eb", # La línea azul que conecta con tu header
        text_align="center",
    )
