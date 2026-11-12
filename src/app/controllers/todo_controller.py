from sqlalchemy.orm import Session

from app.model.todo import Todo, TodoCreate, TodoUpdate

def get_all(db: Session):
    return db.query(Todo).all()