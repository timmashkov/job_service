from sqlalchemy import select, Result, insert
from sqlalchemy.ext.asyncio import AsyncSession

from settings.models import Company
from src.company.schemas import CompanyIn


async def get_companies(session: AsyncSession):
    stmt = select(Company).order_by(Company.id)
    result: Result = await session.execute(stmt)
    answer = result.scalars().all()
    if len(answer) > 0:
        return answer
    return {"answer": "Sorry, there are no companies"}


async def find_company(name: str, session: AsyncSession):
    stmt = select(Company).where(Company.name == name)
    result = await session.execute(stmt)
    await session.commit()
    answer = result.scalars().first()
    if answer:
        return answer
    return {"answer": f"There is no such company as {name}"}


async def insert_company(company: CompanyIn, session: AsyncSession):
    try:
        stmt = (
            insert(Company)
            .values(
                name=company.name,
                description=company.description,
                address=company.address,
                people=company.people,
                hunt_count=company.hunt_count,
                ticker=company.ticker,
            )
            .returning(
                Company.name,
                Company.description,
                Company.address,
                Company.people,
                Company.hunt_count,
                Company.ticker,
            )
        )
        result = await session.execute(stmt)
        answer = result.first()
        if answer:
            await session.commit()
            return answer._asdict()
        else:
            await session.rollback()
        return {"answer": "Cannot add new data"}
    except Exception as e:
        await session.rollback()
        return {"answer": f"Error {e} is caught"}
