from sqlalchemy.orm import Session

from fs.model.todo import Todo, TodoCreate, TodoUpdate

def get_all(db: Session):
    return db.query(Todo).all()

def get_one(db: Session, todo_id: int):
    return db.query(Todo).filter(Todo.id == todo_id).first()

def create(db: Session, data: TodoCreate):
    todo = Todo(**data.model_dump())
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

def update(db: Session, todo_id: int, data: TodoUpdate):
    todo = get_one(db, todo_id)
    if not todo:
        return None
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(todo, key, value)
    db.commit()
    db.refresh(todo)
    return todo

def delete(db: Session, todo_id: int):
    todo = get_one(db, todo_id)
    if not todo:
        return None
    db.delete(todo)
    db.commit()
    return True