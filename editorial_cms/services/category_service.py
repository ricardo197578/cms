from sqlmodel import Session, select
from editorial_cms.database import engine
from editorial_cms.models.post import Post
from editorial_cms.models.category import Category
from editorial_cms.models.categoria_sidebar import CategoriaSidebar
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
    

from sqlmodel import Session, select
from editorial_cms.database import engine
from editorial_cms.models.category import Category
from editorial_cms.models.post import Post


def obtener_categorias_con_contador():

    resultado = []

    with Session(engine) as session:

        categorias = session.exec(select(Category)).all()

        for categoria in categorias:

            cantidad = session.exec(
                select(Post)
                .where(
                    Post.categoria_id == categoria.id,
                    Post.publicado == True,
                )
            ).all()

            resultado.append(
                CategoriaSidebar(
                    id=categoria.id,
                    nombre=categoria.nombre,
                    slug=categoria.slug,
                    cantidad=len(cantidad),
                )
            )

    return resultado