from datetime import datetime, timedelta

from jose import jwt
from passlib.context import CryptContext
from pydantic import EmailStr

from config import ALGORITHM, PASSWORD_SALT, SECRET_KEY, SESSION_TIME
from user.dao import UserDAO

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(text_password, hashed_password) -> bool:
    text_password += PASSWORD_SALT
    return pwd_context.verify(text_password, hashed_password)


def get_password_hash(password) -> str:
    password += PASSWORD_SALT
    return pwd_context.hash(password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=SESSION_TIME)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(
        to_encode, SECRET_KEY, ALGORITHM
    )
    return encoded_jwt


async def auth_user(email: EmailStr, password: str):
    user = await UserDAO.get_or_none(email=email)
    if user:
        if verify_password(password, user.hashed_password):
            return user
