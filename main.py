from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from routers.products_router import router as router_products
from routers.user_router import router as router_user


api = FastAPI()


origins = [
"http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
"http://localhost", "http://localhost:8080", "https://tienda-virtual-app.herokuapp.com"
]

api.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

# Bienvenida
@api.get("/")
async def home():
    return {"message":"Bienvenido a la API de Tienda Virtual."}


api.include_router(router_products)
api.include_router(router_user)
