import secrets
import uuid
from time import time
from typing import Annotated

from fastapi import APIRouter, Depends, status, HTTPException, Header, Response
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

tokens = {"bbb5c512095eb03c4bf77b6590cfacb3": "timur",
          "934f8af2293c8c9318b1b91d6bfa9870": "user"}

cookies: dict[str, dict] = {}
cookie_session_id = "web-api-cookie"

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


def get_username_by_token(token: str = Header(alias="top-secret")):
    if token not in tokens:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Wrong token")
    return tokens[token]


def generate_session_id():
    return uuid.uuid4().hex


@router.get("/auth_header")
def get_credentials_header(auth_username: str = Depends(get_username_by_token)):
    return {"messages": f"Hi {auth_username}"}


@router.post("/login_cookie")
async def login_with_cookie(response: Response,
        auth_username: str = Depends(get_user),
                            ):
    session_id = generate_session_id()
    cookies[session_id] = {"username": auth_username,
                           "login": time()}
    response.set_cookie(cookie_session_id, session_id)
    return {"message": "ok"}


