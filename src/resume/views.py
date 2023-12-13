from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from settings.database import tempest
from settings.models import Resume
from src.resume.dependencies import resume_by_id
from src.resume.schemas import ResumeIn, ResumeOut
from src.resume.service import get_all_resume, insert_resume, update_resume, delete_resume

router = APIRouter(
    prefix="/resume"
)


@router.get("/", response_model=list[ResumeOut])
async def show_resumes(session: AsyncSession = Depends(tempest.async_scoped_session)):
    return await get_all_resume(session=session)


@router.get("/show_resume")
async def show_resume(resume: Resume = Depends(resume_by_id)):
    return resume


@router.post("/create_resume")
async def create_resume(resume: ResumeIn,
                        session: AsyncSession = Depends(tempest.async_scoped_session)):
    return await insert_resume(resume=resume,
                               session=session)


@router.post("/change_resume")
async def change_resume(resume: ResumeIn,
                        session: AsyncSession = Depends(tempest.async_scoped_session)):
    return await update_resume(resume=resume,
                               session=session)


@router.delete("/drop_resume")
async def drop_resume(resume: Resume = Depends(resume_by_id),
                      session: AsyncSession = Depends(tempest.async_scoped_session)):
    return await delete_resume(resume=resume,
                               session=session)
