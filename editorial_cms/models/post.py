from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime
from editorial_cms.models.category import Category


class Post(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    
    titulo: str
    slug: str = Field(index=True, unique=True)

    contenido: str
    autor_id: int

    publicado: bool = Field(default=False)

    creado_en: datetime = Field(default_factory=datetime.utcnow)

    categoria_id: Optional[int] = Field(default=None, foreign_key="category.id")
    categoria: Optional[Category] = Relationship(back_populates="posts")
    
    fecha_publicacion: datetime = Field(default_factory=datetime.utcnow)

    