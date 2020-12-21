from sqlalchemy import Column, String, Boolean
from db.db_conection import Base, engine


class UserInDB(Base):
    __tablename__ = "users"

    usuario = Column(String, primary_key=True, unique=True)
    nombre = Column(String)
    apellido = Column(String)
    password = Column(String)
    rol = Column(String)
    estado = Column(Boolean)


Base.metadata.create_all(bind=engine)
