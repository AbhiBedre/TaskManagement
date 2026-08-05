from src.tasks.dtos import TaskCreateDTO
from sqlalchemy.orm import Session
from src.tasks.models import TaskModel
from fastapi import HTTPException

def create_task(body: TaskCreateDTO, db: Session):
    # print(f"Creating task with title: {body.model_dump()}")
    data = body.model_dump()
    new_task = TaskModel(**data)

    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    # return {"message": "Task created successfully", "data": new_task}
    return new_task

def get_tasks(db: Session):
    tasks = db.query(TaskModel).all()
    # return {"message": "Tasks retrieved successfully", "data": tasks}
    return tasks

def get_task_by_id(task_id: int, db: Session):
    task = db.query(TaskModel).get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    # return {"message": "Task retrieved successfully", "data": task}
    return task

def update_task(task_id: int, body: TaskCreateDTO, db: Session):
    task = db.query(TaskModel).get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Update the task attributes using the model_dump method, user can update single or multiple attributes at once
    for key, value in body.model_dump().items():
        setattr(task, key, value)
    # task.title = body.title
    # task.description = body.description
    # task.is_completed = body.is_completed

    # db.add(task)
    db.commit()
    db.refresh(task)
    # return {"message": "Task updated successfully", "data": task}
    return task

def delete_task(task_id: int, db: Session):
    task = db.query(TaskModel).get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()
    return None