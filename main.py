from fastapi import FastAPI
from src.utils.db import Base, engine
# from src.tasks.models import TaskModel
from src.tasks.router import tasks_router
from src.user.router import user_routes

Base.metadata.create_all(bind=engine)

app = FastAPI(name="My FastAPI Application", description="This is a sample FastAPI application.", version="1.0.0")
app.include_router(tasks_router)
app.include_router(user_routes)

print("\n=== Registered Routes ===")

for route in app.routes:

    print(route.path, route.methods)

print("=========================\n")