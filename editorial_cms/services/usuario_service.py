from sqlmodel import Session, select
from editorial_cms.database import engine
from editorial_cms.models.usuario import Usuario
from editorial_cms.core.security import hash_password


def listar_usuarios():
    with Session(engine) as session:
        return session.exec(select(Usuario)).all()


def crear_usuario(username: str, email: str, password: str, rol: str):
    with Session(engine) as session:
        usuario = Usuario(
            username=username,
            email=email,
            password_hash=hash_password(password),
            rol=rol
        )
        session.add(usuario)
        session.commit()


def eliminar_usuario(user_id: int):
    with Session(engine) as session:
        usuario = session.get(Usuario, user_id)
        if usuario:
            session.delete(usuario)
            session.commit()


def cambiar_estado(user_id: int, activo: bool):
    with Session(engine) as session:
        usuario = session.get(Usuario, user_id)
        if usuario:
            usuario.activo = activo
            session.add(usuario)
            session.commit()