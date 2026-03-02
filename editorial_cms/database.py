from sqlmodel import create_engine, SQLModel
import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:celina653@localhost:5432/editorial_cms"
)

engine = create_engine(DATABASE_URL, echo=False)


def init_db():
    SQLModel.metadata.create_all(engine)