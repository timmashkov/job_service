from pathlib import Path

from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = Path(__file__).parent.parent


class DataBaseConfig(BaseSettings):
    url: str = "sqlite+aiosqlite:///./jobs_db.db"
    echo: bool = True


class AuthJWTConfig(BaseSettings):
    private_key: Path = BASE_DIR / "jwt-private.pem"
    public_key: Path = BASE_DIR / "jwt-public.pem"
    algorythm: str = "RS256"


class EmailConfig(BaseSettings):
    GOOGLE_API_PASS: str = os.getenv("GOOGLE_API_PASS")
    MAIL_PORT: int = os.getenv("MAIL_PORT")
    MAIL_FROM: str = os.getenv("MAIL_FROM")
    MAIL_SERVER: str = os.getenv("MAIL_SERVER")
    MAIL_USERNAME: str = os.getenv("MAIL_USERNAME")


class Config(BaseSettings):
    db: DataBaseConfig = DataBaseConfig()
    email: EmailConfig = EmailConfig()
    auth: AuthJWTConfig = AuthJWTConfig()


config = Config()
