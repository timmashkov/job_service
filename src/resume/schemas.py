from pydantic import BaseModel


class ResumeIn(BaseModel):
    first_name: str
    last_name: str
    age: int
    about: str | None = None
    experience: int | None = None
