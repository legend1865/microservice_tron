from pydantic import BaseModel, ConfigDict


class HistoryGetWallet(BaseModel):
    date: str
    wallet: str

    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)
