from sqlmodel import Session, select
from editorial_cms.database import engine
from editorial_cms.models.category import Category
import re


def generar_slug_categoria(nombre: str):
    slug = nombre.lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"\s+", "-", slug)
    return slug


def crear_categoria(nombre: str):
    with Session(engine) as session:
        slug = generar_slug_categoria(nombre)

        categoria = Category(nombre=nombre, slug=slug)
        session.add(categoria)
        session.commit()


def obtener_categorias():
    with Session(engine) as session:
        return session.exec(select(Category)).all()


def obtener_categoria_por_slug(slug: str):
    with Session(engine) as session:
        return session.exec(
            select(Category).where(Category.slug == slug)
        ).first()