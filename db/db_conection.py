from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from os import environ

#Creando Motor y Conexion con la Base de Datos
SQLALCHEMY_DATABASE_URL = environ['DATABASE_URL']
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#Creacion de la Sesion
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

#Creando Base para la creacion de los modelos
Base = declarative_base()
Base.metadata.schema = "tiendadb"