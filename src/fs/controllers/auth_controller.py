from sqlalchemy.orm import Session

from fs.core.security import hash_password, verify_password, create_access_token
from fs.model.user import User, UserSignup, UserLogin

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_user_by_id(db: Session, id: int):
    return db.query(User).filter(User.id == id).first()

def signup(db: Session, data: UserSignup):
    if get_user_by_email(db, data.email):
        return None
    
    user = User(
        name=data.name,
        email=data.email,
        password=hash_password(data.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def login(db: Session, data: UserLogin):
    user = get_user_by_email(db, data.email)
    if not user or not verify_password(data.password, user.password):
        return None
    return create_access_token(user.id)