from fastapi import APIRouter,status,HTTPException,Depends
from sqlalchemy.orm import Session
from db import get_db
import models
from oauth2 import  get_current_user
from validation import vote


router = APIRouter(
    tags=["Votes"]
)
@router.post("/votes",status_code=status.HTTP_201_CREATED)
def votes(vote:vote,db:Session=Depends(get_db),current_user:int=Depends(get_current_user)):

    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    vote_query = db.query(models.votes).filter(
                   models.votes.votes_posts_id==vote.post_id,models.votes.votes_user_id==current_user.id)
    found_vote = vote_query.first()

    if(vote.dir==1):
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=f"user {current_user} already voted on post{vote.post_id}")
        new_vote = models.votes(votes_posts_id=vote.post_id,votes_user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message":"successfully voted"}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="vote not found")
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"message":"successfully deleted"}

