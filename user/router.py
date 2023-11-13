from fastapi import APIRouter, Response

from config import TOKEN_NAME
from exceptions import (IncorrentEmalOrPasswordException,
                        UserAlreadyExistException)
from user.auth import auth_user, create_access_token, get_password_hash
from user.dao import UserDAO
from user.shemas import SUserLogin, SUserRegister

router = APIRouter(
    prefix="/auth",
    tags=["users"]
)


@router.post("/register")
async def register_user(user_data: SUserRegister) -> dict:
    existing_user = await UserDAO.get_or_none(email=user_data.email)
    if existing_user:
        raise UserAlreadyExistException

    hashed_password = get_password_hash(user_data.password)
    await UserDAO.add(email=user_data.email, hashed_password=hashed_password)
    return {'result': f'User [{user_data.email}] registered'}


@router.post("/login")
async def login_user(responce: Response, user_data: SUserLogin) -> dict:
    print(user_data)
    user = await auth_user(user_data.email, user_data.password)
    # print(user)
    if not user:
        raise IncorrentEmalOrPasswordException
    else:
        access_token = create_access_token({'sub': str(user.id)})
        responce.set_cookie(TOKEN_NAME, access_token, httponly=True)

    return {'access_token': access_token}


@router.post("/logout")
async def logout_user(responce: Response) -> dict:
    responce.delete_cookie(TOKEN_NAME)
    return {'mes': 'user logout'}


'''

@router.get("/me")
async def read_user_me(current_user: User = Depends(get_current_user)):
    return current_user


@router.get("/all-users")
async def get_all_users(current_user: User = Depends(get_current_admin_user)):
    user_list = await UserDAO.find_all()
    return user_list

'''
