
from sqlalchemy import insert

from dao.base import BaseDAO
from database import async_session_maker
from user.models import User


class UserDAO(BaseDAO):
    """ class for User model """
    model = User

    @classmethod
    async def add(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()
