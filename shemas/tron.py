from pydantic import BaseModel


class PostTron(BaseModel):
    address: str
    bandwidth: float | None
    energy: float | None
    balance: float


class GetTron(BaseModel):
    bandwidth: float | None
    energy: float | None
    balance: float
