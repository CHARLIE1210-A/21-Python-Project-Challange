from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import logging

# ================= Logging Config =================
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI()

# ================= MODEL =================
class Task(BaseModel):
    id: int
    title: str
    completed: bool = False
    
tasks: List[Task] = []

# ================= ROUTS =================
@app.get("/")
def home():
    return {"message": "Task API is running!"}

@app.get("/tasks")
def get_tasks():
    logger.info("Fetching all tasks")
    return tasks

@app.post("/tasks")
def create_task(task: Task):
    for tsk in tasks:
        if tsk.id == task.id:
            logger.warning(f"Task with id {task.id} already exists.")
            raise HTTPException(400, "Task ID already exists.")
        
    logger.info(f"Creating task with id: {task.id}")
    tasks.append(task)
    return {"message": "Task created successfully!"}

@app.put("/tasks/{task_id}")
def update_task(task_id: int, update_task: Task):
    for idx, task in enumerate(tasks):
        if task.id == task_id:
            logger.info(f"Updating task with id: {task_id}")
            tasks[idx] = update_task
            return {"message": "Task updated successfully!"}
        
        logger.warning(f"Task with if {task_id} not found for update.")
        raise HTTPException(404, "Task not found.")
    
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            logger.info("Deleting task with id: {task_id}")
            tasks.remove(task)
            return {"message": "Task deleted successfully!"}
        
        logger.warning(f"Task with id {task_id} not found for deletion.")
    raise HTTPException(404, "Task not found.")  


