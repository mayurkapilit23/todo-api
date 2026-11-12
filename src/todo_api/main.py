from fastapi import FastAPI, HTTPException

from src.core.utils.exception_handler import http_exception_handler
from src.features.todo.router import router as todo_router

app = FastAPI()

app.add_exception_handler(HTTPException, http_exception_handler)

# Register API routers
app.include_router(todo_router)


@app.get("/health")
def health_check() -> dict:
    return {"status": True, "message": "Welcome to the Todo API!"}
