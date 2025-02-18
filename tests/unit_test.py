from datetime import datetime, timezone
from unittest.mock import AsyncMock

import pytest
from pymongo import MongoClient

from config import setting
from mongodb.decorator import safe_history


@pytest.fixture(scope="module")
def mongo_client():
    client = MongoClient(f"mongodb://{setting.MONGO_HOST}:{setting.MONGO_PORT}/")
    yield client


@pytest.fixture
def mongodb_history(mongo_client):
    db = mongo_client["tron"]
    return db["test_history"]


@pytest.mark.asyncio
async def test_safe_history_with_real_db(mongodb_history):

    mock_func = AsyncMock(return_value={"some": "data"})

    decorated_func = safe_history(mock_func)

    address = "TBgUr1Mp47xrF7ogQqDK5jtJj7ZM8ZyVYG"
    await decorated_func(address=address)

    mock_func.assert_called_once_with(address=address)

    record_data = {
        "date": str(datetime.now(timezone.utc)),
        "wallet": address,
    }

    inserted_record = mongodb_history.find_one({"wallet": address})
    assert inserted_record is not None
    assert inserted_record["wallet"] == address
