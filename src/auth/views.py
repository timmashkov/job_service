from typing import Annotated

from fastapi import APIRouter
from fastapi.security import HTTPBasic, HTTPBasicCredentials

router = APIRouter(
    prefix="/Auth"
)


security = HTTPBasic()


@router.get("/basic_auth")
async def get_credentials(credentials: Annotated[HTTPBasicCredentials, security]):
    return {"messages": "Hi",
            "name": credentials.username,
            "password": credentials.password}
