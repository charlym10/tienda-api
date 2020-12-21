from pydantic import BaseModel

class UserIn(BaseModel):
    usuario: str
    nombre: str
    apellido: str
    password: str
    rol: str
    estado: bool

class UserOut(BaseModel):
    usuario: str
    nombre: str
    apellido: str
    rol: str
    estado: bool

class UserAuth(BaseModel):
    usuario: str
    password: str