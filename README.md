# Todo API

A small FastAPI service for managing todo items. It exposes REST endpoints to create, list, fetch, and delete todos, along with a simple health-check route.

## Features

- Create a todo item
- List all todo items
- Fetch a single todo item by ID
- Delete a todo item
- Basic health check endpoint

## Tech stack

- Python 3.14+
- FastAPI
- Uvicorn

## Getting started

1. Install dependencies:

   ```bash
   uv sync
   ```

2. Start the development server:

   ```bash
   uv run uvicorn src.todo_api.main:app --reload --host 0.0.0.0 --port 8000
   ```

3. Open the API docs in your browser:

   - http://127.0.0.1:8000/docs
   - http://127.0.0.1:8000/redoc

4. Optional: check the app is running:

   ```bash
   curl http://127.0.0.1:8000/health
   ```

## API overview

The app is mounted under the `/api/v1/todos` route and supports:

- `POST /api/v1/todos`
- `GET /api/v1/todos`
- `GET /api/v1/todos/{todo_id}`
- `DELETE /api/v1/todos/{todo_id}`

## Project structure

```text
src/
├── core/
├── features/
├── todo_api/
└── ...
```

The application entry point is `src/todo_api/main.py`.
