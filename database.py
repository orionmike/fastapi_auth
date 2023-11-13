from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from config import *

# postgresql

# async case
url_object = URL.create(
    "postgresql+asyncpg",
    username=config['db']['db_user'],
    password=config['db']['db_password'],
    host=config['db']['host'],
    database=config['db']['db_name']
)

engine = create_async_engine(url_object)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# sync case
sync_url_object = URL.create(
    "postgresql",
    username=config['db']['db_user'],
    password=config['db']['db_password'],
    host=config['db']['host'],
    database=config['db']['db_name']
)

sync_engine = create_engine(sync_url_object)
sync_session_maker = sessionmaker(sync_engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


def recreate_table_list(table_list, engine):
    for model in table_list:
        try:
            model.__table__.drop(engine)
        except:
            pass
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    Base.metadata.create_all(engine)
