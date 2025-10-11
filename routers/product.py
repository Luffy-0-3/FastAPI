
from fastapi import Depends,HTTPException,APIRouter
from validation import product,updateproduct,returnproduct,votes_count
from sqlalchemy.orm import Session
from db import get_db
import models
from oauth2 import  get_current_user
from sqlalchemy import func

router = APIRouter(
    prefix="/product",
    tags = ["product"]
)

@router.get("",response_model = list[returnproduct])
def get_specified_user_products(db:Session=Depends(get_db),current_user:int = Depends(get_current_user)):
    posts = db.query(models.Post).filter(models.Post.user_id==current_user.id).all()
    return posts

@router.get("/all",response_model = list[votes_count])
# @router.get("/all")
def get_all(db:Session=Depends(get_db),limit:int=15,skip:int=3):
    results = db.query(models.Post,func.count(models.votes.votes_posts_id).label("likes")).join(models.votes,models.votes.votes_posts_id==models.Post.id,
                                         isouter=True).group_by(models.Post.id).limit(limit).offset(skip).all()

    # return results
    # return posts
    return [
        {
            **post.__dict__,
            "likes": likes
        }
        for post, likes in results
    ] 



@router.get("/{id}")
def get_product(id:int,db:Session=Depends(get_db)):

    selected_post = db.query(models.Post).filter(models.Post.id==id).first()
    return selected_post


    
@router.post("/add",response_model = returnproduct)
def add_product(product:product,db:Session=Depends(get_db), current_user: int = Depends(get_current_user)):
    # print(**product.dict())
    print(current_user.email)

    new_post = models.Post( user_id=current_user.id,
    **product.dict()
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
 


@router.put("/update")
def add_product(id_product:int,product_changed:updateproduct,db:Session=Depends(get_db),current_users:int = Depends(get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id==id_product)

    posts = post_query.first()

    if(posts==None):
        raise HTTPException(status_code=404,detail="details not found")
    
    if(posts.user_id!=current_users.id):
        return HTTPException(status_code=401,detail="unautherized to update not ur id")
    
    post_query.update(product_changed.dict(),synchronize_session=False)
    db.commit()

    return post_query.first()



@router.delete("/delete")
def delete_product(id:int,db:Session=Depends(get_db), current_user: int = Depends(get_current_user)):

    posts_query = db.query(models.Post).filter(models.Post.id==id)
    post = posts_query.first()
    if post==None:
        raise HTTPException(status_code=404,detail="cant delete because this id is not present")
    if post.user_id!=current_user.id:
        return HTTPException(status_code=401,detail="unautherized to delete becaause its not ur post")
    
    posts_query.delete(synchronize_session = False)
    db.commit()

    raise HTTPException(status_code=200,detail="successfully deleted")