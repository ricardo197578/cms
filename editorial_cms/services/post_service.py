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