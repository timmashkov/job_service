from fastapi import APIRouter
from .resume.views import router as resume_router

router = APIRouter(
    prefix="/src"
)

router.include_router(router=resume_router, tags=["Resume"])
