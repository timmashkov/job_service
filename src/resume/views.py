from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from settings.database import tempest
from src.resume.schemas import ResumeIn
from src.resume.service import get_all_resume, insert_resume

router = APIRouter(
    prefix="/resume"
)


@router.get("/")
async def show_resumes(session: AsyncSession = Depends(tempest.async_scoped_session)):
    return await get_all_resume(session=session)


@router.post("/create_resume")
async def create_resume(resume: ResumeIn,
                        session: AsyncSession = Depends(tempest.async_scoped_session)):
    return await insert_resume(resume=resume,
                               session=session)
