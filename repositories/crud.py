from tronpy import Tron

from mongodb.mongodb import mongodb_history

client = Tron()


async def get_tron_data(wallet_address: str):
    account_info = client.get_account(wallet_address)
    resources = client.get_account_resource(wallet_address)

    balance = account_info.get("balance", 0)
    bandwidth = resources.get("freeNetRemaining", 0)
    energy = resources.get("EnergyLimit", 0)

    return {"balance": (balance / 1_000_000), "bandwidth": bandwidth, "energy": energy}


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
