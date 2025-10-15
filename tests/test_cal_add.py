import  validation 
from tests.database_testing import session,client


def test_greet(client):
    res = client.get("/")
    # print(res.json())

    assert res.json() ==  "Hello Team Shadow welcome to game"
    

def test_users(client):
    res = client.post("/users",json={"email":"himaja@gmail.com","password":"pass123"})
    new_user = validation.view_user_data(**res.json())
    
    assert new_user.email == "himaja@gmail.com"
