import pytest
from sqlalchemy import insert, select

from settings.models import Resume
from tests.test_sql_app import TestingSessionLocal


@pytest.mark.asyncio
async def add_resume():
    async with TestingSessionLocal() as session:
        stmt = insert(Resume).values(first_name="Timur",
                                     last_name="Mashkov",
                                     age=29,
                                     about="Initial dev",
                                     experience=2)
        await session.commit(stmt)

        query = select(Resume)
        result = await session.execute(query)
        assert result.all() == [("Timur", "Mashkov", 29, "Initial dev", 2)], "Резюме не добавилось"
