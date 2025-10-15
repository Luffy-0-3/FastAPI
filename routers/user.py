from fastapi import APIRouter,Depends,HTTPException,status
from validation import product,updateproduct,returnproduct,users,view_user_data
from sqlalchemy.orm import Session
from db import get_db
import models
from utils import hashed

router = APIRouter(
    tags=["user"]
)

@router.post('/users',response_model=view_user_data)
def user_data(user:users,db:Session=Depends(get_db)):
    try:
        password_hash = hashed(user.password)
        user.password = password_hash

        new_user = models.users(**user.dict())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user
    except:
        raise HTTPException( status.HTTP_305_USE_PROXY,detail="username already exists")


@router.get("/user/{id}",response_model=view_user_data)
def selected_user(id:int,db:Session=Depends(get_db)):
    sel_user = db.query(models.users).filter(models.users.id == id).first()

    if not sel_user:
        raise HTTPException(status_code=404,detail="user id not found")
    return sel_user

