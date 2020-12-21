from fastapi import Depends, APIRouter, HTTPException

from sqlalchemy.orm import Session

from db.db_conection import get_session
from db.users_db import UserInDB


from models.user_models import UserAuth, UserIn, UserOut


router = APIRouter()


@router.get("/api/v1/user")
async def get_user(usuario: str, session: Session = Depends(get_session)):
    user_in_db = session.query(UserInDB).get(usuario)
    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe.")
    user_out = UserOut(**user_in_db.__dict__)
    return  user_out

@router.post("/api/v1/user/auth")
async def auth_user(user_in: UserAuth, db: Session = Depends(get_session)):
    user_in_db = db.query(UserInDB).get(user_in.usuario)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe.")
    
    if user_in_db.password != user_in.password:
        raise HTTPException(status_code=403, detail="Error de autenticacion.")

    return  {"Autenticado": True}
