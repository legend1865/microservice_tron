from datetime import datetime, timezone
from functools import wraps

from models.request_wallet import HistoryGetWallet
from mongodb.mongodb import mongodb_collection


def safe_history(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):

        result = await func(*args, **kwargs)
        record = HistoryGetWallet(
            date=str(datetime.now(timezone.utc)),
            wallet=kwargs.get("address"),
        )
        await mongodb_collection.insert_one(record.model_dump())

        return result

    return wrapper
