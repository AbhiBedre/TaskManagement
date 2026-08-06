from sqlalchemy.orm import Session
from src.user.dtos import UserDTO, LoginSchema
from src.user.models import UserModel
from fastapi import HTTPException, status, Request
from pwdlib import PasswordHash
import jwt
from jwt.exceptions import InvalidTokenError
from src.utils.settings import settings
from datetime import datetime, timedelta

password_hash = PasswordHash.recommended()

def get_password_hash(password):
    return password_hash.hash(password)

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)

def register(db: Session, user_dto: UserDTO):
    is_user = db.query(UserModel).filter(UserModel.username == user_dto.username).first()
    if is_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    is_email = db.query(UserModel).filter(UserModel.email == user_dto.email).first()
    if is_email:
        raise HTTPException(status_code=400, detail="Email already exists")

    hashed_password = get_password_hash(user_dto.password)
    user = UserModel(
        name=user_dto.name,
        username=user_dto.username,
        email=user_dto.email,
        password_hash=hashed_password  # In a real application, you should hash the password
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def login(db: Session, login_schema: LoginSchema):
    user = db.query(UserModel).filter(UserModel.username == login_schema.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")

    # if not password_hash.verify(login_schema.password, user.password_hash):
    #     raise HTTPException(status_code=400, detail="Invalid username or password")
    if not verify_password(login_schema.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")

    exp_time = datetime.now() + timedelta(minutes=settings.EXP_TIME)

    token = jwt.encode(payload={"user_id": user.id, "exp": exp_time.timestamp()}, key=settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    return {"access_token": token, "user_id": user.id}