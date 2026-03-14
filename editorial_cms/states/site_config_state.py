import reflex as rx  # Importa la librería principal de Reflex
# Importa funciones del servicio para obtener y guardar configuración desde la base de datos
from editorial_cms.services.site_config_service import obtener_config, guardar_config


class SiteConfigState(rx.State):  # Define una clase de estado que hereda de rx.State
    LAYOUTS_DISPONIBLES: tuple[str, ...] = ("minimalista", "blog", "revista", "portal")

    # 🔹 CONFIGURACIÓN GENERAL  # Comentario: sección de configuración básica del sitio
    site_name: str = "Editorial CMS"  # Nombre del sitio con valor por defecto
    site_tagline: str = "Portal de artículos y conocimiento"  # Lema o eslogan del sitio

    # 🔹 HERO DEL INDEX  # Comentario: configuración de la sección hero (principal) de la página de inicio
    hero_title: str = "Bienvenido al sitio"  # Título principal de la sección hero
    hero_subtitle: str = "Explora nuestros artículos"  # Subtítulo de la sección hero
    hero_button_text: str = "Ver artículos"  # Texto del botón en la sección hero

    # 🔹 BANNER DE PÁGINAS  # Comentario: configuración del banner que aparece en otras páginas
    banner_title: str = "Artículos"  # Título del banner
    banner_subtitle: str = "Explora nuestros contenidos"  # Subtítulo del banner

    # 🔹 FOOTER  # Comentario: configuración del pie de página
    footer_text: str = "© 2026 Editorial CMS"  # Texto de copyright en el footer

    # 🔹 REDES SOCIALES  # Comentario: URLs de perfiles de redes sociales (vacías por defecto)
    facebook_url: str = ""  # URL de Facebook
    twitter_url: str = ""  # URL de Twitter/X
    youtube_url: str = ""  # URL de YouTube
    linkedin_url: str = ""  # URL de LinkedIn

    # 🔹 LAYOUT PÚBLICO
    layout_publico: str = "minimalista"

    # 🔹 MENSAJES UI  # Comentario: mensajes para mostrar al usuario en la interfaz
    mensaje: str = ""  # Mensaje de confirmación o error (vacío por defecto)



    def cargar_config(self):  # Método para cargar la configuración desde la base de datos

        config = obtener_config()  # Llama al servicio para obtener la configuración

        if not config:  # Si no hay configuración (None o vacío)
            return  # Sale del método sin hacer cambios

        # Asigna cada valor de la configuración obtenida a las variables de estado
        self.site_name = config.site_name  # Actualiza nombre del sitio
        self.site_tagline = config.site_tagline  # Actualiza lema del sitio

        self.hero_title = config.hero_title  # Actualiza título hero
        self.hero_subtitle = config.hero_subtitle  # Actualiza subtítulo hero
        self.hero_button_text = config.hero_button_text  # Actualiza texto del botón hero

        self.banner_title = config.banner_title  # Actualiza título del banner
        self.banner_subtitle = config.banner_subtitle  # Actualiza subtítulo del banner

        self.footer_text = config.footer_text  # Actualiza texto del footer

        self.facebook_url = config.facebook_url  # Actualiza URL de Facebook
        self.twitter_url = config.twitter_url  # Actualiza URL de Twitter
        self.youtube_url = config.youtube_url  # Actualiza URL de YouTube
        self.linkedin_url = config.linkedin_url  # Actualiza URL de LinkedIn
        self.layout_publico = config.layout_publico or "minimalista"



    def guardar(self):  # Método para guardar la configuración en la base de datos

        data = {  # Crea un diccionario con todos los valores actuales del estado
            "site_name": self.site_name,  # Nombre actual del sitio
            "site_tagline": self.site_tagline,  # Lema actual del sitio

            "hero_title": self.hero_title,  # Título hero actual
            "hero_subtitle": self.hero_subtitle,  # Subtítulo hero actual
            "hero_button_text": self.hero_button_text,  # Texto botón hero actual

            "banner_title": self.banner_title,  # Título banner actual
            "banner_subtitle": self.banner_subtitle,  # Subtítulo banner actual

            "footer_text": self.footer_text,  # Texto footer actual

            "facebook_url": self.facebook_url,  # URL Facebook actual
            "twitter_url": self.twitter_url,  # URL Twitter actual
            "youtube_url": self.youtube_url,  # URL YouTube actual
            "linkedin_url": self.linkedin_url,  # URL LinkedIn actual
            "layout_publico": self.layout_publico,
        }

        guardar_config(data)  # Llama al servicio para guardar el diccionario en la base de datos

        self.mensaje = "Configuración guardada correctamente"  # Establece mensaje de éxito



    # 🔹 limpiar mensaje  # Comentario: función para limpiar el mensaje de la interfaz
    def limpiar_mensaje(self):  # Método para borrar el mensaje mostrado
        self.mensaje = ""  # Asigna cadena vacía al mensaje

    def set_layout_publico(self, value: str):
        if value in self.LAYOUTS_DISPONIBLES:
            self.layout_publico = value
