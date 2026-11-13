from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from fs.config.database import get_db
from fs.controllers.todo_controller import get_all, get_one, create, update, delete
from fs.model.todo import TodoCreate, TodoUpdate, TodoResponse

router = APIRouter(prefix="/todos", tags=["Todos"])

@router.get("/", response_model=list[TodoResponse])
def list_todos(db: Session = Depends(get_db)):
    return get_all(db)

@router.get("/{todo_id}", response_model=TodoResponse)
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = get_one(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.post("/", response_model=TodoResponse)
def create_todo(data: TodoCreate, db: Session = Depends(get_db)):
    return create(db, data)

@router.patch("/{todo_id}", response_model=TodoResponse)
def update_todo(todo_id: int, data: TodoUpdate, db: Session = Depends(get_db)):
    todo = update(db, todo_id, data)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.delete("/{todo_id}", response_model=bool)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    if not delete(db, todo_id):
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"success": True}