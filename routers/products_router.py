from fastapi import HTTPException
from fastapi.params import Depends
from fastapi.routing import APIRouter

from typing import List

from sqlalchemy.orm import Session

from db.db_conection import get_session

from db.products_db import ProductInDB

from models.product_models import ProductOut, ProductIn


router = APIRouter()


# Obtener todos los productos
@router.get("/api/v1/products")
async def all_products(session: Session = Depends(get_session)):
    products_in_db = session.query(ProductInDB).order_by(ProductInDB.id)

    products_out: List[ProductOut] = []
    for product in products_in_db:
        product_out = ProductOut(**product.__dict__)
        products_out.append(product_out)
    
    return  products_out

# Obtener un del producto
@router.get("/api/v1/product/{id}")
async def get_product(id: int, session: Session = Depends(get_session)):
    product_in_db = session.query(ProductInDB).get(id)
    if product_in_db == None:
        raise HTTPException(status_code=404, detail="El producto no existe.")
    product_out = ProductOut(**product_in_db.__dict__)
    return  product_out

# Crear producto
@router.post("/api/v1/product", status_code=201)
async def create_product(product: ProductIn, session: Session = Depends(get_session)):
    product_in_db = ProductInDB(**product.dict())

    # Create
    session.add(product_in_db)
    session.commit()
    session.refresh(product_in_db)
    
    product_out = ProductOut(**product_in_db.__dict__)

    return product_out

# Actualizar producto
@router.put("/api/v1/product")
async def update_product(product: ProductOut, session: Session = Depends(get_session)):
    product_in_db = session.query(ProductInDB).get(product.id)

    if product_in_db == None:
        raise HTTPException(status_code=404,detail='El producto no existe.')
    else:
        # Update
        product_in_db.nombre = product.nombre
        product_in_db.categoria = product.categoria
        product_in_db.precio = product.precio
        product_in_db.unidad = product.unidad
        product_in_db.proveedor = product.proveedor
        product_in_db.disponibilidad = product.disponibilidad
        product_in_db.url = product.url
        
        session.commit()
        session.refresh(product_in_db)

        product_out = ProductOut(**product_in_db.__dict__)

        return product_out