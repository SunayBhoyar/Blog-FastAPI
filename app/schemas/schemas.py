from pydantic import BaseModel
from typing import List

# Blog base
class Blog(BaseModel):
    title: str
    body: str
    class Config:
        orm_mode = True

# User base
class User(BaseModel):
    name: str
    email: str
    password: str

# Blog with creator
class BlogShow(BaseModel):
    title: str
    body: str
    creator: 'UserShow'  
    class Config:
        orm_mode = True

# User with blog list
class UserShow(BaseModel):
    id: int
    name: str
    email: str
    blogs: List[Blog] = []
    class Config:
        orm_mode = True

class UserUpdate(User):
    old_password : str
    class Config:
        orm_mode = True

class login(BaseModel):
    email: str 
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username : str | None = None

