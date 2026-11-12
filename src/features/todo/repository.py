# In-memory database
from src.features.todo.model import Todo

todos_db: dict[int, Todo] = {}


class TodoRepository:
    @staticmethod
    def get_todo_by_id(todo_id: int) -> Todo | None:
        return todos_db.get(todo_id)

    @staticmethod
    def create_todo(todo: Todo) -> Todo:
        todos_db[todo.id] = todo
        return todo

    @staticmethod
    def get_all_todos() -> list[Todo]:
        return list(todos_db.values())

    @staticmethod
    def delete_todo_by_id(todo_id: int) -> bool:
        if todo_id in todos_db:
            del todos_db[todo_id]
            return True
        return False