from pydantic_settings import BaseSettings


class DataBaseConfig(BaseSettings):
    url: str = "sqlite+aiosqlite:///./jobs_db.db"
    echo: bool = True


class Config(BaseSettings):
    db: DataBaseConfig = DataBaseConfig()


config = Config()
