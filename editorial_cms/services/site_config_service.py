from sqlmodel import Session, select
from editorial_cms.database import engine
from editorial_cms.models.site_config import SiteConfig


def obtener_config():

    with Session(engine) as session:

        config = session.exec(
            select(SiteConfig)
        ).first()

        return config


def guardar_config(data):

    with Session(engine) as session:

        config = session.exec(
            select(SiteConfig)
        ).first()

        if not config:

            config = SiteConfig(**data)
            session.add(config)

        else:

            config.site_name = data["site_name"]
            config.site_tagline = data["site_tagline"]
            config.hero_title = data["hero_title"]
            config.hero_subtitle = data["hero_subtitle"]
            config.hero_button_text = data["hero_button_text"]
            config.banner_title = data["banner_title"]
            config.banner_subtitle = data["banner_subtitle"]
            config.footer_text = data["footer_text"]
            config.facebook_url = data["facebook_url"]
            config.twitter_url = data["twitter_url"]
            config.youtube_url = data["youtube_url"]
            config.linkedin_url = data["linkedin_url"]
            config.layout_publico = data["layout_publico"]

        session.commit()
