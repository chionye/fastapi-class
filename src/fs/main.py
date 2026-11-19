from fastapi import FastAPI

from fs.config.database import engine, Base
from fs.middleware.auth_middleware import JWTAuthMiddleware
from fs.routes import auth_routes, todo_routes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Todo API", version="1.0.0")

app.add_middleware(JWTAuthMiddleware)

app.include_router(todo_routes.router)
app.include_router(auth_routes.router)

@app.get("/")
def health():
    return {"status": "ok", "message": "Todo API is running!"}