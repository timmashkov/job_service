from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from settings.models import Resume


async def get_all_resume(session: AsyncSession):
    stmt = select(Resume).order_by(Resume.id)
    result = await session.execute(stmt)
    answer = result.scalars().all()
    return answer
