from asyncio import current_task

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
    AsyncSession,
)

from settings.config import config


class DataBase:
    def __init__(self):
        self.engine = create_async_engine(url=config.db.url, echo=config.db.echo)
        self.session_fabric = async_sessionmaker(
            bind=self.engine, autoflush=False, autocommit=False, expire_on_commit=False
        )

    def async_scoped_session(self):
        session = async_scoped_session(
            session_factory=self.session_fabric, scopefunc=current_task
        )
        return session

    async def scoped_session_point(self) -> AsyncSession:
        session = self.async_scoped_session()
        yield session
        await session.close()


tempest = DataBase()
