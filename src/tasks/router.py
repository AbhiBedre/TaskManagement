from fastapi import APIRouter, Depends
from src.tasks import controllers
from src.tasks.dtos import TaskCreateDTO
from src.utils.db import get_db

tasks_router = APIRouter(prefix="/tasks")

@tasks_router.post("/create")
def create_task(body: TaskCreateDTO, db = Depends(get_db)):
    return controllers.create_task(body, db)

@tasks_router.get("/all_tasks")
def get_tasks(db = Depends(get_db)):
    return controllers.get_tasks(db)

@tasks_router.get("/one_task/{task_id}")
def get_task_by_id(task_id: int, db = Depends(get_db)):
    return controllers.get_task_by_id(task_id, db)

@tasks_router.put("/update_task/{task_id}")
def update_task(task_id: int, body: TaskCreateDTO, db = Depends(get_db)):
    return controllers.update_task(task_id, body, db)

@tasks_router.delete("/delete_task/{task_id}")
def delete_task(task_id: int, db = Depends(get_db)):
    return controllers.delete_task(task_id, db)