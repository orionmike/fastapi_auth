
from sqlalchemy import Column, Integer, String
from database import Base, engine, recreate_table_list


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False)
    # email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
