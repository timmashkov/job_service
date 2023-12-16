from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()


class DataBaseConfig(BaseSettings):
    url: str = "sqlite+aiosqlite:///./jobs_db.db"
    echo: bool = True


class EmailConfig(BaseSettings):
    GOOGLE_API_PASS: str = os.getenv("GOOGLE_API_PASS")
    MAIL_PORT: int = os.getenv("MAIL_PORT")
    MAIL_FROM: str = os.getenv("MAIL_FROM")
    MAIL_SERVER: str = os.getenv("MAIL_SERVER")
    MAIL_USERNAME: str = os.getenv("MAIL_USERNAME")


class Config(BaseSettings):
    db: DataBaseConfig = DataBaseConfig()
    email: EmailConfig = EmailConfig()


config = Config()
