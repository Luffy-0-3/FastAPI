from fastapi import FastAPI,Depends
from validation import product
import models
from db import engine
from sqlalchemy.orm import Session
from db import get_db
from routers import product,user,auth
from config import setting
import votes
from fastapi.middleware.cors import CORSMiddleware

# print(setting.database_username)


# models.Base.metadata.create_all(bind=engine)

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)
app.include_router(product.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(votes.router)




@app.get("/")
def greet():
    return "Hello Team Shadow welcome to game"

@app.get("/st")
def trail(db:Session=Depends(get_db)):
    posts = db.query(models.Post).all()
    return "connected to db ",posts

# products=[
#     product(id = 1,name="apple",description="awwesomme",price=9999,quantity=1),
#    product(id = 2,name="cake",description="avg",price=999,quantity=2),
#    product(id = 3,name="pineapple",description="nice",price=9399,quantity=4),
#    product(id = 4,name="papaya",description="bad",price=4599,quantity=3)
# ]

# @app.get("/product/{id}")
# def get_product(id:int,db:Session=Depends(get_db)):
#     for product in products:
#         if product.id == id:
#             return product
#     else:
#         return "incorrect id"

# @app.put("/update")
# def add_product(id_product:int,product_changed:product):
#     for i in range(len(products)):
#         if products[i].id == id_product:
#             products[i]=product_changed
#             return "product added successfully"
#     return "product not found"


# @app.post("/add")
# def add_product(product:product): #product class datatypes 
#     products.append(product)
#     return product


# @app.post("/add")
# def add_product(product:product,db:Session=Depends(get_db)):
#     # print(**product.dict())
#     new_post = models.Post( 
#         name=product.name,description=product.description, price= product.price,quantity=product.quantity
#     )
#     db.add(new_post)
#     db.commit()
#     db.refresh(new_post)




# @app.delete("/delete")
# def delete_product(id:int):
#     for i in range(len(products)):
#         if products[i].id==id:
#             products.pop(id-1)
#             return "deleted sucessfully"
#     return "not possible"




