from celery import Celery
from fastapi_mail import MessageSchema, MessageType, FastMail
from starlette.responses import JSONResponse

from src.email.config import conf
from src.email.schema import EmailSchema

celery = Celery("email", broker="redis://localhost:6379")


@celery.task
def sending(email: EmailSchema) -> JSONResponse:
    html = """<p>Hi this test mail, thanks for using Async Job service</p> """

    message = MessageSchema(
        subject="Async Job Service",
        recipients=email.model_dump().get("email"),
        body=html,
        subtype=MessageType.html)

    fm = FastMail(conf)
    fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})
