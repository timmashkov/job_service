from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from settings.database import tempest
from settings.models import Resume
from src.resume.service import find_resume


async def resume_by_id(
    name: Annotated[str, Path],
    session: AsyncSession = Depends(tempest.async_scoped_session),
) -> Resume:
    product = await find_resume(session=session, name=name)
    if product is not None:
        return product

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Resume {name} not found!",
    )
