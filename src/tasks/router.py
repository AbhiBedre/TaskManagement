from fastapi import APIRouter
from src.tasks import controllers

tasks_router = APIRouter(prefix="/tasks")

@tasks_router.post("/create")
def create_task():
    return controllers.create_task()