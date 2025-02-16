from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base

from config import setting

async_engine = create_async_engine(
    url=setting.db_url_async,
)

new_session = async_sessionmaker(async_engine)

Base = declarative_base()
