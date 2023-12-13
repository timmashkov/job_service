from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from settings.models import Company


async def get_companies(session: AsyncSession):
    stmt = select(Company).order_by(Company.id)
    result: Result = await session.execute(stmt)
    answer = result.scalars().all()
    if len(answer) > 0:
        return answer
    return {"answer": "Sorry, there are no companies"}
