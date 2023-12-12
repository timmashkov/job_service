from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from settings.models import Resume
from src.resume.schemas import ResumeIn


async def get_all_resume(session: AsyncSession):
    stmt = select(Resume).order_by(Resume.id)
    result = await session.execute(stmt)
    answer = result.scalars().all()
    return answer


async def insert_resume(resume: ResumeIn,
                        session: AsyncSession):
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
