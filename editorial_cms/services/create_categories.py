from sqlmodel import Session, select
from editorial_cms.database import engine
from editorial_cms.models.category import Category


def crear_categorias():

    categorias = [
        {"nombre": "Tecnología", "slug": "tecnologia"},
        {"nombre": "Programación", "slug": "programacion"},
        {"nombre": "Inteligencia Artificial", "slug": "inteligencia-artificial"},
        {"nombre": "Ciencia", "slug": "ciencia"},
        {"nombre": "Tutoriales", "slug": "tutoriales"},
        {"nombre": "Historia", "slug": "historia"},
    ]

    with Session(engine) as session:

        

        

        for cat in categorias:

            print("Revisando:", cat["nombre"])

            existe = session.exec(
                select(Category).where(Category.slug == cat["slug"])
            ).first()

            if not existe:
                print("Creando:", cat["nombre"])
                session.add(Category(**cat))

        session.commit()
