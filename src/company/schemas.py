from pydantic import BaseModel


class CompanyIn(BaseModel):
    name: str
    description: str
    address: str
    people: int | None = None
    hunt_count: int
    ticker: str | None = None


class CompanyOut(CompanyIn):
    id: int
