from fastapi import APIRouter,Depends,HTTPException
from validation import user_login
from sqlalchemy.orm import Session
from db import get_db
import models,oauth2
from fastapi.security import OAuth2PasswordRequestForm
from utils import verify_password

router = APIRouter(
    tags=["auth"]
                    )

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(),db:Session=Depends(get_db)):
    login = db.query(models.users).filter(models.users.email==form_data.username).first()

    if not login:
        raise HTTPException(status_code=404,detail="invalid email")
    
    if not verify_password(form_data.password,login.password):
        raise HTTPException(status_code=404,detail="wrong pass")
    

    token = oauth2.create_access_token(data = {"user_id":login.id})
    return {"access_token":token,"token_type":"bearer"}




