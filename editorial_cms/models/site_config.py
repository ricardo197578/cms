from sqlmodel import SQLModel, Field
from typing import Optional


class SiteConfig(SQLModel, table=True):

    id: Optional[int] = Field(default=1, primary_key=True)

    site_name: str
    site_tagline: str
    hero_title: str
    hero_subtitle: str
    hero_button_text: str
    footer_text: str

    banner_title: str
    banner_subtitle: str

    facebook_url: str
    twitter_url: str
    youtube_url: str
    linkedin_url: str
    layout_publico: str = Field(default="minimalista")
