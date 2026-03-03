from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Post(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    titulo: str
    contenido: str

    autor_id: int

    creado_en: datetime = Field(default_factory=datetime.utcnow)