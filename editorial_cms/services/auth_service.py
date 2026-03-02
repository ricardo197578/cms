from sqlmodel import Session, select
from editorial_cms.models.usuario import Usuario
from editorial_cms.database import engine
from editorial_cms.core.security import verify_password


def autenticar_usuario(username: str, password: str):
    with Session(engine) as session:
        statement = select(Usuario).where(Usuario.username == username)
        usuario = session.exec(statement).first()

        if not usuario:
            return None

        if not verify_password(password, usuario.password_hash):
            return None

        return usuario