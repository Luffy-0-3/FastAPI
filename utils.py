from passlib.context import CryptContext
password_context = CryptContext(schemes=["argon2"],deprecated="auto")

def hashed(password:str):
    return password_context.hash(password)

def verify_password(plain_password,hashed_password):
    return password_context.verify(plain_password,hashed_password)