from pydantic import BaseModel

class CategoriaSidebar(BaseModel):
    id: int
    nombre: str
    slug: str
    cantidad: int