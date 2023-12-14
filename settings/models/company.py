from datetime import datetime

from sqlalchemy import String, func, Integer, Text

from settings.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column


class Company(Base):
    __tablename__ = "company"

    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    address: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    people: Mapped[int] = mapped_column(Integer, nullable=True)
    hunt_count: Mapped[int] = mapped_column(Integer, nullable=False)
    ticker: Mapped[str] = mapped_column(String(7), nullable=True, unique=True)
