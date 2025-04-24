from fastapi import APIRouter , status , Depends  
from ..schemas import schemas
from sqlalchemy.orm import Session
from ..db.createDatabase import get_db
from typing import List
from ..repository import user

router =  APIRouter(
    prefix = '/user',
    tags=['users']
) 

@router.post('/create', status_code=status.HTTP_201_CREATED,response_model=schemas.UserShow)
def create_user(request : schemas.User, db : Session = Depends(get_db)):
    return user.create_user(request , db)

@router.get('/get/{id}' ,status_code=status.HTTP_202_ACCEPTED)
def get_by_id_user(id: int ,db : Session = Depends(get_db)):
    return user.get_by_id_user(id ,db)


@router.get('/getAll' ,status_code=status.HTTP_202_ACCEPTED , response_model=List[schemas.UserShow])
def get_all_users(db : Session = Depends(get_db)):
   return user.get_all_users(db)

@router.put('/update/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_user(id : int ,request : schemas.UserUpdate, db : Session = Depends(get_db)):
    return user.update_user(id, request , db)
    
@router.delete('/delete/{id}' , status_code= status.HTTP_202_ACCEPTED)
def delete_user(id:int ,password : str, db : Session = Depends(get_db)):
    return delete_user(id, password ,db)