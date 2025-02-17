import datetime

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


class HistoryTron(BaseModel):
    date: datetime.datetime
    wallet: str


class GetHistoryTron(BaseModel):
    total: int
    page: int
    size: int
    items: list[HistoryTron]
