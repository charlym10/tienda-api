from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#Creando Motor y Conexion con la Base de Datos
SQLALCHEMY_DATABASE_URL = "postgresql://ercytalbqsojwx:f9bf08755a5eff3bb869027e7ddaccf6d4ca67ef59dcaa266c6e34be212b606d@ec2-34-194-198-238.compute-1.amazonaws.com:5432/d9am7r4dmb7efi"
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