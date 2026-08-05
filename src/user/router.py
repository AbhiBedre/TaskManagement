from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.user import controllers
from src.user.dtos import UserDTO, UserResponseDTO, LoginSchema
from src.utils.db import get_db

user_routes = APIRouter(prefix="/user")

@user_routes.post("/register", response_model=UserResponseDTO, status_code=status.HTTP_201_CREATED)
def register(user_dto: UserDTO, db: Session = Depends(get_db)):
    user = controllers.register(db, user_dto)
    return user

@user_routes.post("/login")
def login(login_schema: LoginSchema, db: Session = Depends(get_db), status_code=status.HTTP_200_OK):
    return controllers.login(db, login_schema)