
from pydantic import BaseModel, EmailStr


class SUserRegister(BaseModel):
    email: EmailStr
    password: str


class SUserLogin(BaseModel):
    email: EmailStr
    password: str
