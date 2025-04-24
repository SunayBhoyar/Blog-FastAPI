from fastapi import APIRouter , Depends,HTTPException , status
from ..JWToken import create_access_token
from sqlalchemy.orm import Session
from ..schemas import schemas
from fastapi.security import OAuth2PasswordRequestForm 
from ..db.createDatabase import get_db
from ..models import userModel
from ..hashing import hash

router = APIRouter(
    tags = ['Autentication']
)

@router.post('/login')
def login(request : OAuth2PasswordRequestForm = Depends() , db : Session = Depends(get_db)):
    user_fetch = db.query(userModel.User).filter(userModel.User.email == request.username).first()
    if not user_fetch :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f'user with email id : {request.username} is not found')
    elif not hash.Hash.verify(user_fetch.password,request.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials. Please check your password."
        )
    access_token = create_access_token(data={"sub": user_fetch.email})
    return schemas.Token(access_token=access_token, token_type="bearer")


    return user_fetch 