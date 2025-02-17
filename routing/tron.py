from fastapi import APIRouter, HTTPException, Query
from tronpy import Tron

from mongodb.decorator import safe_history
from mongodb.mongodb import mongodb_history
from repositories.crud import add_new_wallet, get_history_wallet, get_tron_data
from shemas.tron import GetHistoryTron, GetTron, HistoryTron, PostTron

router = APIRouter(
    prefix="/tron",
    tags=["/tron"],
)

client = Tron()


@router.post("/register")
async def register_tron_address(add_wallet: PostTron):
    wallet_model = await add_new_wallet(add_wallet)
    if not wallet_model:
        raise HTTPException(status_code=404, detail="address not found")

    return wallet_model


@router.get("/wallet")
@safe_history
async def get_data(
    address: str,
) -> GetTron:
    tron_get_model = await get_tron_data(address)
    if not tron_get_model:
        raise HTTPException(status_code=404, detail="Wallet not found")

    return tron_get_model


@router.get("/history")
async def get_history(address: str, page: int = 1, limit: int = 5) -> GetHistoryTron:
    history_wallet = await get_history_wallet(address, page, limit)

    return history_wallet
