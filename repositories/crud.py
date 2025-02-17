from sqlalchemy import select

from db import new_session
from models.tron_model import Tron
from mongodb.mongodb import mongodb_history


async def get_tron_data(address):
    async with new_session() as session:
        wallet_model = await session.scalar(
            select(Tron).filter(Tron.address == address)
        )

        return wallet_model


async def add_new_wallet(add_wallet):
    async with new_session() as session:
        new_wallet_model = add_wallet.model_dump()
        new_wallet = Tron(**new_wallet_model)
        session.add(new_wallet)
        await session.commit()
        await session.refresh(new_wallet)
        return new_wallet


async def get_history_wallet(address: str, page: int, limit: int):
    mongo_cursor = (
        mongodb_history.find({"wallet": address})
        .sort("date", -1)
        .skip(limit * (page - 1))
        .limit(limit)
    )

    total_history = await mongodb_history.count_documents({"wallet": address})

    histories = await mongo_cursor.to_list(length=None)
    return {
        "total": total_history,
        "page": page,
        "size": limit,
        "items": histories,
    }
