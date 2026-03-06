from typing import Optional, List, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from editorial_cms.models.post import Post


class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    slug: str = Field(index=True, unique=True)

    posts: List["Post"] = Relationship(back_populates="categoria")