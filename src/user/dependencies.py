
from datetime import datetime

from fastapi import Depends, Request
from jose import JWTError, jwt

from config import ALGORITHM, SECRET_KEY, TOKEN_NAME
from exceptions import (IncorrectTokenFormatException, TokenAbsentException,
                        TokenExpiresException, UserIsNotPresentException)
from user.dao import UserDAO
from user.models import User


def get_token(request: Request):
    token = request.cookies.get(TOKEN_NAME)
    if not token:
        raise TokenAbsentException
    else:
        return token


async def get_current_user(token: str = Depends(get_token)):

    payload = {}

    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
    except JWTError:
        IncorrectTokenFormatException

    expire: str = payload.get('exp')
    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise TokenExpiresException

    user_id: str = payload.get('sub')
    if not user_id:
        raise UserIsNotPresentException

    user = await UserDAO.get_by_id(int(user_id))
    if not user:
        raise UserIsNotPresentException
    else:
        return user


async def get_current_admin_user(current_user: User = Depends(get_current_user)):
    return current_user
