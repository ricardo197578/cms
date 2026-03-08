from sqlalchemy.orm import selectinload
from sqlmodel import Session, select
from editorial_cms.database import engine
from editorial_cms.models.post import Post
from editorial_cms.models.category import Category
import re

def crear_post(titulo, contenido, autor_id, categoria_id):
    with Session(engine) as session:

        slug = generar_slug_unico(titulo)

        nuevo = Post(
            titulo=titulo,
            slug=slug,
            contenido=contenido,
            autor_id=autor_id,
            categoria_id=categoria_id
        )

        session.add(nuevo)
        session.commit()

def obtener_posts():
    with Session(engine) as session:
        statement = select(Post)
        return session.exec(statement).all()


def obtener_posts_por_autor(autor_id: int):
    with Session(engine) as session:
        statement = select(Post).where(Post.autor_id == autor_id)
        return session.exec(statement).all()


def obtener_post_por_id(post_id: int):
    with Session(engine) as session:
        return session.get(Post, post_id)


def eliminar_post(post_id: int):
    with Session(engine) as session:
        post = session.get(Post, post_id)
        if post:
            session.delete(post)
            session.commit()


def actualizar_post(post_id: int, titulo: str, contenido: str):
    with Session(engine) as session:
        post = session.get(Post, post_id)
        if post:
            post.titulo = titulo
            post.contenido = contenido
            session.add(post)
            session.commit()


def toggle_publicado(post_id: int):
    with Session(engine) as session:
        post = session.get(Post, post_id)
        if post:
            post.publicado = not post.publicado
            session.add(post)
            session.commit()

def obtener_publicados():
    with Session(engine) as session:
        statement = select(Post).where(Post.publicado == True)
        return session.exec(statement).all()
    
def obtener_publicados():
    with Session(engine) as session:
        return session.exec(
            select(Post)
            .where(Post.publicado == True)
            .order_by(Post.fecha_publicacion.desc())
        ).all()
    
def generar_slug_base(titulo: str) -> str:
    slug = titulo.lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"\s+", "-", slug)
    return slug


def generar_slug_unico(titulo: str) -> str:
    slug_base = generar_slug_base(titulo)
    slug = slug_base
    contador = 1

    with Session(engine) as session:
        while True:
            statement = select(Post).where(Post.slug == slug)
            existe = session.exec(statement).first()

            if not existe:
                break

            slug = f"{slug_base}-{contador}"
            contador += 1

    return slug

def obtener_post_por_slug(slug: str):
    with Session(engine) as session:
        statement = (
            select(Post)
            .where(Post.slug == slug)
            .options(selectinload(Post.categoria))
        )
        return session.exec(statement).first()
    
def obtener_posts_por_categoria(categoria_id: int):
    with Session(engine) as session:
        return session.exec(
            select(Post)
            .where(Post.categoria_id == categoria_id)
            .where(Post.publicado == True)
        ).all()
    
def obtener_posts_por_categoria_slug(slug: str):
    with Session(engine) as session:
        statement = (
            select(Post)
            .join(Category)
            .where(Category.slug == slug)
            .where(Post.publicado == True)
            .options(selectinload(Post.categoria))
        )
        return session.exec(statement).all()
    
def obtener_recientes(limit: int = 5):
    with Session(engine) as session:
        return session.exec(
            select(Post)
            .where(Post.publicado == True)
            .order_by(Post.fecha_publicacion.desc())
            .limit(limit)
        ).all()

 #Funcion de busqueda que se extiende en PublicState
def buscar_posts_por_titulo(texto: str):
    with Session(engine) as session:
        statement = (
            select(Post)
            .where(
                Post.publicado == True,
                Post.titulo.ilike(f"%{texto}%")
            )
            .order_by(Post.fecha_publicacion.desc())
        )
        return session.exec(statement).all()

def buscar_posts(
    texto: str = "",
    categoria_slug: str = "",
    page: int = 1,
    per_page: int = 5,
):
    with Session(engine) as session:
        statement = select(Post).where(Post.publicado == True)

        if texto:
            statement = statement.where(
                (Post.titulo.ilike(f"%{texto}%")) |
                (Post.contenido.ilike(f"%{texto}%"))
            )

        if categoria_slug:
            from editorial_cms.models.category import Category
            statement = statement.join(Category).where(
                Category.slug == categoria_slug
            )

        statement = statement.order_by(Post.fecha_publicacion.desc())

        # paginación
        offset = (page - 1) * per_page
        statement = statement.offset(offset).limit(per_page)

        return session.exec(statement).all()

from sqlalchemy import func

def contar_posts(texto: str = "", categoria_slug: str = ""):
    with Session(engine) as session:
        statement = select(func.count()).select_from(Post).where(Post.publicado == True)

        if texto:
            statement = statement.where(
                (Post.titulo.ilike(f"%{texto}%")) |
                (Post.contenido.ilike(f"%{texto}%"))
            )

        if categoria_slug:
            from editorial_cms.models.category import Category
            statement = statement.join(Category).where(
                Category.slug == categoria_slug
            )

        return session.exec(statement).one()