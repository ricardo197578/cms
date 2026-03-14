from pydantic import BaseModel


class PostPublic(BaseModel):
    id: int | None = None
    titulo: str
    slug: str
    contenido: str
    fecha_publicacion: str
    imagen_destacada: str | None = None
