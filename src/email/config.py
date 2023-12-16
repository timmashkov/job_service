from fastapi_mail import ConnectionConfig

from settings.config import config

conf = ConnectionConfig(
    MAIL_USERNAME=config.email.MAIL_USERNAME,
    MAIL_PASSWORD=config.email.GOOGLE_API_PASS,
    MAIL_FROM=config.email.MAIL_FROM,
    MAIL_PORT=config.email.MAIL_PORT,
    MAIL_SERVER=config.email.MAIL_SERVER,
    MAIL_FROM_NAME="Async job service",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
)
