from jose import JWTError,jwt
from datetime import datetime,timedelta
from validation import tokendata
from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from db import get_db
import models
from config import setting

oauth2_schemes =OAuth2PasswordBearer(tokenUrl="login") 

SECRET_KEY = setting.secret_key
ALGORITHM = setting.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = setting.access_token_expire_minutes

def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})

    encoded = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded

def verify_access_token(token:str,credentials_exception):
    try:
        payload = jwt.decode(token,SECRET_KEY, algorithms=[ALGORITHM])
        id = payload.get("user_id")

        if id is None:
            raise credentials_exception
        token_data = tokendata(id=str(id))

    except JWTError:
        raise credentials_exception
    return token_data
    
    
def get_current_user(token:str = Depends(oauth2_schemes),db:Session=Depends(get_db)):
    credentials_exception  = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Could not validate credentials or token expired",headers={"WWW-Authenticate":"Bearer"})

    token = verify_access_token(token,credentials_exception)
    user = db.query(models.users).filter(models.users.id == token.id).first()
    return user
    

