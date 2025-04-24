from fastapi import APIRouter , status , Depends  
from ..schemas import schemas
from sqlalchemy.orm import Session
from ..db.createDatabase import get_db
from typing import List
from ..oAuth2 import get_current_user
from ..repository import blog

router = APIRouter(
    prefix = '/blog',
    tags=['blogs']
) 


@router.post('/create',status_code=status.HTTP_201_CREATED )
def crete_blog(request: schemas.Blog, db : Session = Depends(get_db),current_user : schemas.User = Depends(get_current_user)):
    return blog.create_blog(request,db)

@router.get('/get/{id}',status_code=status.HTTP_200_OK,response_model=schemas.BlogShow)
def get_by_id_blog(id:int ,db : Session = Depends(get_db),current_user : schemas.User = Depends(get_current_user)):
    return blog.get_by_id_blog(id  , db)

@router.get('/getall',response_model=List[schemas.BlogShow])
def get_all_blogs(db : Session = Depends(get_db),current_user : schemas.User = Depends(get_current_user)):
    return blog.get_all_blogs(db)


@router.put('/upadte/{id}',status_code=status.HTTP_202_ACCEPTED)
def update_title_blog(id:int ,request : schemas.Blog , db : Session = Depends(get_db),current_user : schemas.User = Depends(get_current_user)):
    return blog.update_title_blog(id, request , db)

@router.delete('/delete/{id}',status_code=status.HTTP_202_ACCEPTED)
def delete_blog(id:int , db : Session = Depends(get_db),current_user : schemas.User = Depends(get_current_user)):
    return blog.delete_blog(id,db)




