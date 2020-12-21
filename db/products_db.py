from sqlalchemy import Column, Integer, String, Float
from db.db_conection import Base, engine


class ProductInDB(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, unique=True)
    nombre = Column(String)
    categoria = Column(String)
    precio = Column(Float)
    unidad = Column(String)
    proveedor = Column(String)
    disponibilidad = Column(Integer)
    url = Column(String)


Base.metadata.create_all(bind=engine)