from fastapi import APIRouter
from .resume.views import router as resume_router
from .company.views import router as company_router
from .auth.views import router as auth_router
from .email.views import router as mail_router

router = APIRouter(prefix="/src")

router.include_router(router=resume_router, tags=["Resume"])
router.include_router(router=company_router, tags=["Company"])
router.include_router(router=auth_router, tags=["Auth"])
router.include_router(router=mail_router, tags=["Email"])
