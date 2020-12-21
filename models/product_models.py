from pydantic import BaseModel

class ProductOut(BaseModel):
    id: int
    nombre: str
    categoria: str
    precio: int
    unidad: str
    proveedor: str
    disponibilidad: int
    url: str

class ProductIn(BaseModel):
    nombre: str
    categoria: str
    precio: int
    unidad: str
    proveedor: str
    disponibilidad: int
    url: str

class ProductCant(BaseModel):
    nombre: str
    disponibilidad: int
