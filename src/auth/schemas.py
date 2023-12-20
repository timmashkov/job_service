from pydantic import BaseModel, Field, ConfigDict


class UserSchema(BaseModel):
    model_config = ConfigDict(strict=True)
    username: str = Field(le=3, ge=25)
    password: bytes
    email: str | None
    active: bool = True
