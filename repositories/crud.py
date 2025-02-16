from sqlalchemy import select

from db import new_session
from models.tron_model import Tron


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
