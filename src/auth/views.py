import secrets
from typing import Annotated

from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials

router = APIRouter(
    prefix="/Auth"
)


security = HTTPBasic()


@router.get("/basic_auth")
def get_credentials(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    return {"messages": "Hi",
            "name": credentials.username,
            "password": credentials.password}


database = {"timur": 'hello', "user": 'user'}


def get_user(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    unauth_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                     detail="Wrong username or password",
                                     headers={"WWW-Authenticate": "Basic"})
    correct_pass = database.get(credentials.username)
    if correct_pass is None:
        raise unauth_exception
    if not secrets.compare_digest(credentials.password.encode("utf-8"), correct_pass.encode("utf-8")):
        raise unauth_exception
    return credentials.username


@router.get("/auth_user")
def get_credentials_username(auth_username: str = Depends(get_user)):
    return {"messages": f"Hi {auth_username}"}
