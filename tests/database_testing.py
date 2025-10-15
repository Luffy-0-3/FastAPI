from fastapi.testclient import TestClient
from main import app
from fastapi import status

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from db import get_db,Base
import pytest



sqlalchemy_dataabase_url = "postgresql://postgres:shadow_19@localhost:5432/testing"
engine = create_engine(sqlalchemy_dataabase_url)

testingsessionlocal = sessionmaker(autoflush=False,autocommit=False,bind=engine)

@pytest.fixture
def session():
     Base.metadata.drop_all(bind=engine)
     Base.metadata.create_all(bind=engine)
     db = testingsessionlocal()
     try:
         yield db
     finally:
         db.close()   


@pytest.fixture
def client(session):
    def override_get_db():
        try:
            yield session   
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    
