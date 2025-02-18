from fastapi import APIRouter, HTTPException

from mongodb.decorator import safe_history
from repositories.crud import get_history_wallet, get_tron_data
from shemas.tron import GetHistoryTron, GetTron

router = APIRouter(
    prefix="/tron",
    tags=["/tron"],
)


@router.post("/wallet")
@safe_history
async def get_data(
    address: str,
) -> GetTron:
    tron_get = await get_tron_data(address)
    if not tron_get:
        raise HTTPException(status_code=404, detail="Wallet not found")

    return tron_get


@router.get("/history")
async def get_history(address: str, page: int = 1, limit: int = 5) -> GetHistoryTron:
    history_wallet = await get_history_wallet(address, page, limit)

    return history_wallet
