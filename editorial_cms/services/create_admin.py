from sqlmodel import Session
from editorial_cms.database import engine
from editorial_cms.models.usuario import Usuario
from editorial_cms.core.security import hash_password

def crear_admin():
    with Session(engine) as session:
        admin = Usuario(
            username="admin",
            email="admin@cms.com",
            password_hash=hash_password("123456"),
            rol="admin",
            activo=True
        )

        session.add(admin)
        session.commit()

        print("Superadmin creado correctamente.")

if __name__ == "__main__":
    crear_admin()