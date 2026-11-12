from fastapi import HTTPException, status

from src.features.todo.model import Todo
from src.features.todo.repository import TodoRepository
from src.features.todo.schemas import TodoCreate


class TodoService:
    def __init__(self, repository: TodoRepository):
        self.repository = repository

    def create_todo(self, todo_create: TodoCreate) -> Todo:

        return self.repository.create_todo(
            Todo(
                id=len(self.repository.get_all_todos()) + 1,
                title=todo_create.title,
                description=todo_create.description,
            )
        )

    def get_todos(self) -> list[Todo]:
        return self.repository.get_all_todos()

    def get_todo_by_id(self, todo_id: int) -> Todo | None:
        if todo_id <= 0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid todo ID")
        return self.repository.get_todo_by_id(todo_id)

    def delete_todo_by_id(self, todo_id: int) -> bool:
        if todo_id <= 0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid todo ID")
        return self.repository.delete_todo_by_id(todo_id)
