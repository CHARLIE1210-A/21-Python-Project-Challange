# Task Manager API

This project is part of the "21 Python Project Challenge" and represents application 15: a simple Task Manager API built with FastAPI.

## Features
- Create, read, update, and delete tasks
- Each task has an `id`, `title`, and `completed` status
- Logging for key actions and errors
- RESTful endpoints

## Endpoints

| Method | Endpoint           | Description                |
|--------|--------------------|----------------------------|
| GET    | `/`                | Health check               |
| GET    | `/tasks`           | List all tasks             |
| POST   | `/tasks`           | Create a new task          |
| PUT    | `/tasks/{task_id}` | Update an existing task    |
| DELETE | `/tasks/{task_id}` | Delete a task              |

## Example Task Object
```
{
  "id": 1,
  "title": "Learn FastAPI",
  "completed": false
}
```

## Usage

1. Install dependencies:
   ```bash
   pip install fastapi uvicorn pydantic
   ```

2. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

3. Access the API:
   - Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for interactive Swagger UI.

## Project Structure
```
main.py
pyproject.toml
README.md
```

## Logging
- Logs are printed to the console for actions like creating, updating, and deleting tasks.

## License
This project is for educational purposes as part of the 21 Python Project Challenge.
