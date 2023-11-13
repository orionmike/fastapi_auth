from database import async_session_maker
from sqlalchemy import select, insert


class BaseDAO:
    """ base class for working with the database """
    model = None

    @classmethod
    async def get_by_id(cls, model_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=int(model_id))
            object = await session.execute(query)
            return object.scalar_one_or_none()

    @classmethod
    async def get_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            object = await session.execute(query)
            return object.scalar_one_or_none()

    @classmethod
    async def get_list(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            object_list = await session.execute(query)
            return object_list.scalars().all()
