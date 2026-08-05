from fastapi import APIRouter, Depends, status, Request
from sqlalchemy.orm import Session
from src.user import controllers
from src.user.dtos import UserDTO, UserResponseDTO, LoginSchema
from src.utils.db import get_db

user_routes = APIRouter(prefix="/user")

@user_routes.post("/register", response_model=UserResponseDTO, status_code=status.HTTP_201_CREATED)
def register(user_dto: UserDTO, db: Session = Depends(get_db)):
    user = controllers.register(db, user_dto)
    return user

@user_routes.post("/login", status_code=status.HTTP_200_OK)
def login(login_schema: LoginSchema, db: Session = Depends(get_db)):
    return controllers.login(db, login_schema)

@user_routes.get("/is_auth", response_model=UserResponseDTO, status_code=status.HTTP_200_OK)
def is_authenticated(request: Request, db: Session = Depends(get_db)):
    return controllers.is_authenticated(request, db)