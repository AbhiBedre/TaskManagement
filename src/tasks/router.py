from fastapi import APIRouter, Depends, status
from src.tasks import controllers
from src.tasks.dtos import TaskCreateDTO, TaskResponseDTO
from src.utils.db import get_db
from sqlalchemy.orm import Session
from src.utils.helpers import is_authenticated
from src.user.models import UserModel

tasks_router = APIRouter(prefix="/tasks")

@tasks_router.post("/create", response_model=TaskResponseDTO, status_code=status.HTTP_201_CREATED)
def create_task(body: TaskCreateDTO, db: Session = Depends(get_db), user: UserModel = Depends(is_authenticated)):
    return controllers.create_task(body, db, user)

@tasks_router.get("/all_tasks", response_model=list[TaskResponseDTO], status_code=status.HTTP_200_OK)
def get_tasks(db: Session = Depends(get_db), user: UserModel = Depends(is_authenticated)):
    return controllers.get_tasks(db, user)

@tasks_router.get("/one_task/{task_id}", response_model=TaskResponseDTO, status_code=status.HTTP_200_OK)
def get_task_by_id(task_id: int, db: Session = Depends(get_db), user: UserModel = Depends(is_authenticated)):
    return controllers.get_task_by_id(task_id, db)

@tasks_router.put("/update_task/{task_id}", response_model=TaskResponseDTO, status_code=status.HTTP_200_OK)
def update_task(task_id: int, body: TaskCreateDTO, db: Session = Depends(get_db), user: UserModel = Depends(is_authenticated)):
    return controllers.update_task(task_id, body, db, user)

@tasks_router.delete("/delete_task/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db), user: UserModel = Depends(is_authenticated)):
    return controllers.delete_task(task_id, db, user)