from fastapi import FastAPI

from fs.config.database import engine, Base
from fs.routes.todo_routes import router as todo_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Todo API", version="1.0.0")

app.include_router(todo_router)

@app.get("/")
def health():
    return {"status": "ok", "message": "Todo API is running!"}