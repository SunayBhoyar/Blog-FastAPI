from fastapi import FastAPI
from app.models import blogModel
from app.db.createDatabase import engine

from app.router import blog , user , authentication

app = FastAPI() 

blogModel.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)


