from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from settings.database import tempest
from src.resume.service import get_all_resume

router = APIRouter(
    prefix="/resume"
)


@router.get("/")
async def show_resumes(session: AsyncSession = Depends(tempest.async_scoped_session)):
    return await get_all_resume(session=session)
