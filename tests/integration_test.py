import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient

from main import app

client = TestClient(app)


@pytest.mark.asyncio
async def test_get_wallet_data():
    async with AsyncClient(base_url="http://test") as ac:
        response = await ac.post(
            "http://127.0.0.1:8000/tron/wallet",
            params={"address": "TBgUr1Mp47xrF7ogQqDK5jtJj7ZM8ZyVYG"},
        )

    assert response.status_code == 200
    json_response = response.json()
    assert "balance" in json_response
    assert "bandwidth" in json_response
    assert "energy" in json_response
