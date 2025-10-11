from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import setting
import os

# sqlalchemy_dataabase_url = f"postgresql://{setting.database_username}:{setting.database_password}@{setting.database_hostname}:{setting.database_port}/{setting.database_name}"
# engine = create_engine(sqlalchemy_dataabase_url)

SQLALCHEMY_DATABASE_URL = setting.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

sessionlocal = sessionmaker(autoflush=False,autocommit=False,bind=engine)

Base = declarative_base()


#dependency ---->we will use everytime when we need to connect to db
def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()
