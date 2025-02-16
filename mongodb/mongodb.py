from motor.motor_asyncio import AsyncIOMotorClient

from config import setting

mongodb_client = AsyncIOMotorClient(
    f"mongodb://{setting.MONGO_HOST}:{setting.MONGO_PORT}/"
)
mongodb_db = mongodb_client.get_database("tron")
mongodb_collection = mongodb_db.get_collection("history")
