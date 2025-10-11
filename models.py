from sqlalchemy import Column,String,Integer,Float,TIMESTAMP,ForeignKey
from sqlalchemy.sql.expression import null,text
from db import Base
from sqlalchemy.orm import Relationship

class Post(Base):
    __tablename__="groceries"
    id = Column(Integer,primary_key=True,nullable=False,autoincrement=True)
    name = Column(String,nullable=False)
    description = Column(String,nullable=False)
    price = Column(Float,nullable=False)
    quantity = Column(Integer,nullable=False)
    user_id = Column(Integer,ForeignKey("users_data.id",ondelete="CASCADE"),nullable=False)

    owner = Relationship("users")


class users(Base):
    __tablename__ = "users_data"
    id = Column(Integer,primary_key=True,nullable=False,autoincrement=True)
    email = Column(String,nullable=False,unique=True)
    password = Column(String(500),nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))

class votes(Base):
    __tablename__ = "votes"

    votes_user_id = Column(Integer,ForeignKey("users_data.id",ondelete="CASCADE"),primary_key=True)
    votes_posts_id = Column(Integer,ForeignKey("groceries.id",ondelete="CASCADE"),primary_key=True)




