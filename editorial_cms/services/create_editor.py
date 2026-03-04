from sqlmodel import Session
from editorial_cms.database import engine
from editorial_cms.models.usuario import Usuario
from editorial_cms.core.security import hash_password


def crear_editor():
    with Session(engine) as session:

        editor = Usuario(
            username="editor",
            email="editor@cms.com",
            password_hash=hash_password("editor123"),
            rol="editor",
            activo=True
        )

        session.add(editor)
        session.commit()

        print("Usuario editor creado correctamente.")


if __name__ == "__main__":
    crear_editor()