from sqlalchemy import select, insert, update
from sqlalchemy.ext.asyncio import AsyncSession

from settings.models import Resume
from src.resume.schemas import ResumeIn


async def get_all_resume(session: AsyncSession):
    stmt = select(Resume).order_by(Resume.id)
    result = await session.execute(stmt)
    answer = result.scalars().all()
    if len(answer) > 0:
        return answer
    return {"answer": "Sorry, there are no resumes"}


async def find_resume(name: str,
                      session: AsyncSession):
    try:
        stmt = select(Resume).where(Resume.first_name == name)
        result = await session.execute(stmt)
        await session.commit()
        answer = result.first()
        return answer._asdict()
    except Exception as e:
        await session.rollback()
        return {"answer": f"Error {e} is catched"}


async def insert_resume(resume: ResumeIn,
                        session: AsyncSession):
    try:
        stmt = (insert(Resume)
                .values(first_name=resume.first_name,
                        last_name=resume.last_name,
                        age=resume.age,
                        about=resume.about,
                        experience=resume.experience)
                .returning(Resume.id,
                           Resume.first_name,
                           Resume.last_name,
                           Resume.age,
                           Resume.about,
                           Resume.experience,
                           Resume.created_at))
        result = await session.execute(stmt)
        await session.commit()
        answer = result.first()
        return answer._asdict()
    except Exception as e:
        await session.rollback()
        return {"answer": f"Error {e} is catched"}


async def update_resume(resume: ResumeIn,
                        session: AsyncSession):
    try:
        stmt = (update(Resume)
                .values(first_name=resume.first_name,
                        last_name=resume.last_name,
                        age=resume.age, about=resume.about,
                        experience=resume.experience)
                .where(Resume.first_name == resume.first_name)
                .returning(Resume.id,
                           Resume.first_name,
                           Resume.last_name,
                           Resume.age,
                           Resume.about,
                           Resume.experience,
                           Resume.created_at))
        result = await session.execute(stmt)
        await session.commit()
        answer = result.first()
        return answer._asdict()
    except Exception as e:
        await session.rollback()
        return {"answer": f"Error {e} is catched"}
    