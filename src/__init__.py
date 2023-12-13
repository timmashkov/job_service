from fastapi import APIRouter
from .resume.views import router as resume_router
from .company.views import router as company_router

router = APIRouter(
    prefix="/src"
)

router.include_router(router=resume_router, tags=["Resume"])
router.include_router(router=company_router, tags=["Company"])
