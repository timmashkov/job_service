from datetime import datetime

from sqlalchemy import String, func, Integer, Text

from settings.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column


class Resume(Base):
    __tablename__ = 'worker'

    first_name: Mapped[str] = mapped_column(String(20), nullable=False)
    last_name: Mapped[str] = mapped_column(String(20), nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    about: Mapped[str] = mapped_column(Text, nullable=True)
    experience: Mapped[int] = mapped_column(Integer, nullable=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now(), default=datetime.now)
