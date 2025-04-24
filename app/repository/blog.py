from fastapi import status , Depends, HTTPException , Response  
from ..db.createDatabase import get_db
from sqlalchemy.orm import Session
from ..models import blogModel
from ..schemas import schemas


def create_blog(request: schemas.Blog, db : Session = Depends(get_db)):
    new_blog = blogModel.Blog(title = request.title, body = request.body,user_id  = 2)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def get_by_id_blog(id:int ,db : Session = Depends(get_db)):
    blog = db.query(blogModel.Blog).filter(blogModel.Blog.id == id).first()
    if not blog :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f'blog with id : {id} is not found')
    return blog

def get_all_blogs(db : Session = Depends(get_db)):
    blogs = db.query(blogModel.Blog).all()
    return blogs 

def update_title_blog(id:int ,request : schemas.Blog , db : Session = Depends(get_db)):
    blog = db.query(blogModel.Blog).filter(blogModel.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f'blog with id : {id} is not found')
    else:
        db.query(blogModel.Blog).filter(blogModel.Blog.id == id).update(request.model_dump())
        db.commit()
        return {'status' : 'updated successfully'}
    
def delete_blog(id:int , db : Session = Depends(get_db)):
    blog = db.query(blogModel.Blog).filter(blogModel.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f'blog with id : {id} is not found')
    else:
        db.query(blogModel.Blog).filter(blogModel.Blog.id == id).delete(synchronize_session=False)
        db.commit()
        return {'status' : 'deleted successfully'}