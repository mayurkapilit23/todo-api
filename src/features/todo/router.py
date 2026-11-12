from fastapi import APIRouter, status

from src.core.schemas.common import ApiResponse
from src.core.utils.response import success_response
from src.features.todo.model import Todo
from src.features.todo.repository import TodoRepository
from src.features.todo.schemas import TodoCreate, TodoResponse
from src.features.todo.service import TodoService

router = APIRouter()


router = APIRouter(prefix="/api/v1/todos", tags=["Todos"])


@router.post("", response_model=ApiResponse[TodoResponse], status_code=status.HTTP_201_CREATED)
def create_todo(create_todo: TodoCreate) -> ApiResponse[TodoResponse]:
    """
    Create a new todo item.
    """
    repository = TodoRepository()
    service = TodoService(repository)
    new_todo = service.create_todo(create_todo)

    return success_response(
        message="Todo created successfully",
        data=TodoResponse(
            id=new_todo.id, title=new_todo.title, description=new_todo.description
        ),
    )


@router.get("", response_model=ApiResponse[list[TodoResponse]], status_code=status.HTTP_200_OK)
def get_todos() -> ApiResponse[list[TodoResponse]]:
    """
    Retrieve all todo items.
    """
    repository = TodoRepository()
    service = TodoService(repository)
    todos = service.get_todos()

    return success_response(
        message="Todos retrieved successfully",
        data=[
            TodoResponse(id=todo.id, title=todo.title, description=todo.description)
            for todo in todos
        ],
    )


@router.get("/{todo_id}", response_model=ApiResponse[TodoResponse], status_code=status.HTTP_200_OK)
def get_todo(todo_id: int) -> ApiResponse[TodoResponse]:
    """
    Retrieve a todo item by its ID.
    """
    repository = TodoRepository()
    service = TodoService(repository)
    todo = service.get_todo_by_id(todo_id)

    if not todo:
        return success_response(message="Todo not found", data=None)

    return success_response(
        message="Todo retrieved successfully",
        data=TodoResponse(id=todo.id, title=todo.title, description=todo.description),
    )

@router.delete("/{todo_id}", response_model=ApiResponse[None], status_code=status.HTTP_200_OK)
def delete_todo(todo_id: int) -> ApiResponse[None]:
    """
    Delete a todo item by its ID.
    """
    repository = TodoRepository()
    service = TodoService(repository)
    success = service.delete_todo_by_id(todo_id)

    if not success:
        return success_response(message="Todo not found", data=None)

    return success_response(message="Todo deleted successfully", data=None)