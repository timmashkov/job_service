import asyncio
from typing import AsyncGenerator

import pytest
from httpx import AsyncClient
from sqlalchemy import StaticPool
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from fastapi.testclient import TestClient
from main import app
from settings.database import tempest
from settings.models import Base

TESTING_DATABASE_URL = "sqlite+aiosqlite:///./test_db.db"

engine = create_async_engine(
    TESTING_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = async_sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine,
                                         expire_on_commit=False,
                                         class_=AsyncSession)


async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with tempest.async_scoped_session() as session:
        yield session


app.dependency_overrides[tempest.async_scoped_session] = override_get_async_session


@pytest.fixture(autouse=True, scope='session')
async def prepare_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope='session')
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


client = TestClient(app)


@pytest.fixture(scope="session")
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
