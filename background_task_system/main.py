import time
import logging
from fastapi import FastAPI, BackgroundTasks

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# ================= BACKGROUND JOB =================
def long_task(task_name: str):
    logger.info(f"Starting long task: {task_name}")
    time.sleep(5)
    logger.info(f"Completed long task: {task_name}")
    
# ================= ROUTES =================
@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI background task example!"}

@app.post("/start-task")
def start_task(task_name: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(long_task, task_name)
    return {"message": f"Task '{task_name}' has been started in the background."}

