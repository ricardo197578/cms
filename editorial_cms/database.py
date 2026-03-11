#from sqlmodel import create_engine, SQLModel
#from editorial_cms.models.site_config import SiteConfig
#import os

#DATABASE_URL = os.getenv(
#    "DATABASE_URL",
#    "postgresql://postgres:celina653@localhost:5432/editorial_cms"
#)

#engine = create_engine(DATABASE_URL, echo=False)

#Registrar modelo
#def init_db():
#    SQLModel.metadata.create_all(engine)


#PRODUCCION
from sqlmodel import create_engine, SQLModel
import os
from dotenv import load_dotenv

# cargar variables .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
    DATABASE_URL,
    echo=False,
    pool_pre_ping=True,   # verifica si la conexión sigue viva
    pool_recycle=300      # recicla conexiones cada 5 minutos
)

def init_db():
    SQLModel.metadata.create_all(engine)

print("DATABASE_URL:", DATABASE_URL)
