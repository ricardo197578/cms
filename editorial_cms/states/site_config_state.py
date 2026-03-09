import reflex as rx
from editorial_cms.services.site_config_service import obtener_config, guardar_config


class SiteConfigState(rx.State):

    # 🔹 CONFIGURACIÓN GENERAL
    site_name: str = "Editorial CMS"
    site_tagline: str = "Portal de artículos y conocimiento"

    # 🔹 HERO DEL INDEX
    hero_title: str = "Bienvenido al sitio"
    hero_subtitle: str = "Explora nuestros artículos"
    hero_button_text: str = "Ver artículos"

    # 🔹 BANNER DE PÁGINAS
    banner_title: str = "Artículos"
    banner_subtitle: str = "Explora nuestros contenidos"

    # 🔹 FOOTER
    footer_text: str = "© 2026 Editorial CMS"

    # 🔹 REDES SOCIALES
    facebook_url: str = ""
    twitter_url: str = ""
    youtube_url: str = ""
    linkedin_url: str = ""

    # 🔹 MENSAJES UI
    mensaje: str = ""



    def cargar_config(self):

        config = obtener_config()

        if not config:
            return

        self.site_name = config.site_name
        self.site_tagline = config.site_tagline

        self.hero_title = config.hero_title
        self.hero_subtitle = config.hero_subtitle
        self.hero_button_text = config.hero_button_text

        self.banner_title = config.banner_title
        self.banner_subtitle = config.banner_subtitle

        self.footer_text = config.footer_text

        self.facebook_url = config.facebook_url
        self.twitter_url = config.twitter_url
        self.youtube_url = config.youtube_url
        self.linkedin_url = config.linkedin_url



    def guardar(self):

        data = {
            "site_name": self.site_name,
            "site_tagline": self.site_tagline,

            "hero_title": self.hero_title,
            "hero_subtitle": self.hero_subtitle,
            "hero_button_text": self.hero_button_text,

            "banner_title": self.banner_title,
            "banner_subtitle": self.banner_subtitle,

            "footer_text": self.footer_text,

            "facebook_url": self.facebook_url,
            "twitter_url": self.twitter_url,
            "youtube_url": self.youtube_url,
            "linkedin_url": self.linkedin_url,
        }

        guardar_config(data)

        self.mensaje = "Configuración guardada correctamente"



    # 🔹 limpiar mensaje
    def limpiar_mensaje(self):
        self.mensaje = ""