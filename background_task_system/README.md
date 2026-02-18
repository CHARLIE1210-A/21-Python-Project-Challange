# Python 21 Project Challenge

This repository contains 19 applications as part of the Python 21 Project Challenge. Each application demonstrates a different concept or use-case in Python, helping you to learn and practice Python programming through hands-on projects.

## Application: Background Task System

This application demonstrates how to use FastAPI's background task system to run long-running tasks asynchronously, without blocking the main application thread.

### Features
- FastAPI web server
- Background task execution using FastAPI's `BackgroundTasks`
- Logging for task start and completion

### How It Works
- The `/` endpoint returns a welcome message.
- The `/start-task` endpoint accepts a `task_name` and starts a long-running task in the background. The task simulates a time-consuming operation using `time.sleep`.

### How to Run
1. **Install dependencies** (if not already installed):
   ```bash
   pip install fastapi uvicorn
   ```
2. **Start the server:**
   ```bash
   python -m uvicorn main:app --reload
   ```
3. **Test the endpoints:**
   - Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser for the welcome message.
   - Use a tool like [Postman](https://www.postman.com/) or `curl` to POST to `/start-task` with a `task_name` parameter:
     ```bash
     curl -X POST "http://127.0.0.1:8000/start-task?task_name=ExampleTask"
     ```

### Example Response
```
{"message": "Task 'ExampleTask' has been started in the background."}
```

### Logging Output
You will see logs in the console indicating when the background task starts and completes.

---

## About the Python 21 Project Challenge
This challenge is designed to help you build 21 different Python applications, each focusing on a unique topic or technology. This repository currently contains 19 of those applications. Each project is self-contained and includes its own documentation and instructions.

Feel free to explore, run, and modify the projects to enhance your Python skills!

---

**Author:** [Your Name Here]
**Date:** February 18, 2026
