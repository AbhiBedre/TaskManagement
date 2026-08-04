from fastapi import FastAPI
from src.utils.db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(name="My FastAPI Application", description="This is a sample FastAPI application.", version="1.0.0")