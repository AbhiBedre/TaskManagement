from src.tasks.dtos import TaskCreateDTO
from sqlalchemy.orm import Session
from src.tasks.models import TaskModel
from src.user.models import UserModel
from fastapi import HTTPException

def create_task(body: TaskCreateDTO, db: Session, user: UserModel):
    # print(f"Creating task with title: {body.model_dump()}")
    data = body.model_dump()
    # new_task = TaskModel(**data)
    new_task = TaskModel(
        title=data.get("title"),
        description=data.get("description"),
        is_completed=data.get("is_completed", False),
        user_id=user.id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    # return {"message": "Task created successfully", "data": new_task}
    return new_task

def get_tasks(db: Session, user: UserModel):
    # tasks = db.query(TaskModel).all()
    tasks = db.query(TaskModel).filter(TaskModel.user_id == user.id).all()
    # return {"message": "Tasks retrieved successfully", "data": tasks}
    return tasks

def get_task_by_id(task_id: int, db: Session):
    task = db.query(TaskModel).get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    # return {"message": "Task retrieved successfully", "data": task}
    return task

def update_task(task_id: int, body: TaskCreateDTO, db: Session, user: UserModel):
    task = db.query(TaskModel).get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if task.user_id != user.id:
        raise HTTPException(status_code=403, detail="You are not authorized to update this task")

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

    if task.user_id != user.id:
        raise HTTPException(status_code=403, detail="You are not authorized to delete this task")

    db.delete(task)
    db.commit()
    return None