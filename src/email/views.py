from fastapi import APIRouter, BackgroundTasks, UploadFile, File, Form
from fastapi_mail import MessageSchema, MessageType, FastMail
from pydantic import EmailStr
from starlette.responses import JSONResponse

from src.email.celery_send import sending
from src.email.config import conf
from src.email.schema import EmailSchema

router = APIRouter(
    prefix="/email"
)


@router.post("/email")
async def simple_send(email: EmailSchema, text: str) -> JSONResponse:
    html = f"""<p>{text}</p> """

    message = MessageSchema(
        subject="Async Job Service",
        recipients=email.model_dump().get("email"),
        body=html,
        subtype=MessageType.html,
    )

    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})


@router.post("/file")
async def send_file(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    email: EmailStr = Form(...),
) -> JSONResponse:
    message = MessageSchema(
        subject="Async Job Service",
        recipients=[email],
        body="Simple background task",
        subtype=MessageType.html,
        attachments=[file],
    )

    fm = FastMail(conf)

    background_tasks.add_task(fm.send_message, message)

    return JSONResponse(status_code=200, content={"message": "email has been sent"})


@router.post("/celery_send")
def celery_send(data: EmailSchema):
    sending(email=data)
    return {"status": 200, "data": "Email has been sent", "details": None}
