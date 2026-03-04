from sqlmodel import Session, select
from editorial_cms.database import engine
from editorial_cms.models.post import Post


def crear_post(titulo, contenido, autor_id):
    with Session(engine) as session:
        nuevo = Post(
            titulo=titulo,
            contenido=contenido,
            autor_id=autor_id
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