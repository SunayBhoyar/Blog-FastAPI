from fastapi import  status , Depends, HTTPException  
from ..schemas import schemas
from sqlalchemy.orm import Session
from ..db.createDatabase import get_db
from ..models import userModel
from ..hashing import hash

def create_user(request : schemas.User, db : Session = Depends(get_db)):
    new_user = userModel.User(name = request.name , email = request.email , password = hash.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
def get_by_id_user(id: int ,db : Session = Depends(get_db)):
    user = db.query(userModel.User).filter(userModel.User.id == id).first()
    if not user: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f'user with id : {id} is not found')
    return user 

def get_all_users(db : Session = Depends(get_db)):
    users = db.query(userModel.User).all()
    return users 

def update_user(id : int ,request : schemas.UserUpdate, db : Session = Depends(get_db)):
    user_fetch = db.query(userModel.User).filter(userModel.User.id == id).first()
    if not user_fetch:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f'user with id : {id} is not found')
    elif not hash.Hash.verify(user_fetch.password, request.old_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials. Please check your old password."
        )
    else : 
        db.query(userModel.User).filter(userModel.User.id == id).update({userModel.User.name : request.name, userModel.User.email : request.email , userModel.User.password : hash.Hash.bcrypt(request.password)})
        db.commit()
        return {'status' : 'updated successfully'}
    
def delete_user(id:int ,password : str, db : Session = Depends(get_db)):
    user_fetch = db.query(userModel.User).filter(userModel.User.id == id).first()
    if not user_fetch :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f'user with id : {id} is not found')
    elif not hash.Hash.verify(user_fetch.password, password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials. Please check your password."
        )
    else:
        db.query(userModel.User).filter(userModel.User.id == id).delete(synchronize_session=False)
        db.commit()
        return {'status' : 'deleted successfully'}