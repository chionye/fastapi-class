from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="My FastAPI Application",
    description="This is a sample FastAPI application.",
    version="1.0.0",
)

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def home():
    return {
        "status": "success", 
        "message": "Welcome to the home page, rocki!", 
        "data": 
            {
            "info": "This is a sample FastAPI application."
            }
        }

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {
        "status": "success",
        "message": f"You requested an item {item_id}.",
        "data": {"item_id": item_id}
    }