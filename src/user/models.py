
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)  # Column(Integer, primary_key=True, nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)  # Column(String, nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
