from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from settings.database import tempest
from src.company.service import get_companies

router = APIRouter(
    prefix="/company"
)


@router.get("/")
async def show_companies(session: AsyncSession = Depends(tempest.async_scoped_session)):
    return await get_companies(session=session)
