from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime


class Usuario(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    username: str = Field(index=True, unique=True)
    email: str = Field(unique=True)

    password_hash: str

    rol: str = "autor"  # superadmin, admin, editor, autor

    activo: bool = True
    fecha_creacion: datetime = Field(default_factory=datetime.utcnow)