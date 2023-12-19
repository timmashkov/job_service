from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from settings.database import tempest
from src.company.schemas import CompanyIn
from src.company.service import get_companies, find_company, insert_company, update_company, delete_company

router = APIRouter(prefix="/company")


@router.get("/")
async def show_companies(session: AsyncSession = Depends(tempest.async_scoped_session)):
    return await get_companies(session=session)


@router.get("/show_company")
async def show_company(
    name: str, session: AsyncSession = Depends(tempest.async_scoped_session)
):
    return await find_company(name=name, session=session)


@router.post("/add_company")
async def add_company(company: CompanyIn,
                      session: AsyncSession = Depends(tempest.async_scoped_session)):
    return await insert_company(company=company, session=session)


@router.put("/change_company")
async def change_company(company_name: str,
                         company: CompanyIn,
                         session: AsyncSession = Depends(tempest.async_scoped_session)):
    return await update_company(company=company,
                                session=session,
                                name=company_name)


@router.delete("/del_company")
async def del_company(corp_name: str,
                      session: AsyncSession = Depends(tempest.async_scoped_session)):
    return await delete_company(name=corp_name, session=session)
