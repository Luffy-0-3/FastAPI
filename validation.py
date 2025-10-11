from pydantic import BaseModel,Field,EmailStr,conint
from datetime import datetime
from typing import Optional

class product(BaseModel):
    name:str
    description:str
    price:float
    quantity:int

class updateproduct(BaseModel):
    name:str
    description:str
    price:float
    quantity:int

class users(BaseModel):
    email : EmailStr
    # password : str

class returnproduct(BaseModel):
    # id:Optional[int]
    name:str
    description:str
    quantity:int
    user_id : int
    owner : users
    class Config:
        orm_mode = True

class votes_count(BaseModel):
    name:str
    description:str
    quantity:int
    user_id : int
    likes:int
    

class users(BaseModel):
    email : EmailStr
    # password : str

class view_user_data(BaseModel):
    id : int
    email : EmailStr
    created_at : datetime
    class Config:
        orm_mode = True

class user_login(BaseModel):
    email : EmailStr
    password : str

class token(BaseModel):
    access_token : str
    token_type : str


class  tokendata(BaseModel):
    id : Optional[str]=None

class vote(BaseModel):
    post_id : int
    dir: conint(le=1)  #type:ignore


    