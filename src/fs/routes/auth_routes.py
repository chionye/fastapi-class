from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from fs.config.database import get_db
from fs.controllers import auth_controller
from fs.model.user import UserSignup, UserLogin, UserResponse, TokenResponse

router = APIRouter(prefix="/auth", tag=["Auth"])

@router.post("/signup", response_model = UserResponse, status_code=201)
def signup(data: UserSignup, db: Session = Depends(get_db)):
    user = auth_controller.signup(db, data)
    if not user:
        raise HTTPException(status_code=400, detail="Email already exists")
    return user

@router.post("/login", response_model = TokenResponse)
def login(data: UserSignup, db: Session = Depends(get_db)):
    token = auth_controller.login(db, data)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid Email or Password")
    return {"access_token": token}

@router.post("/me", response_model = UserResponse)
def me(request: UserSignup, db: Session = Depends(get_db)):
    user = auth_controller.get_user_by_id(db, request.state.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user