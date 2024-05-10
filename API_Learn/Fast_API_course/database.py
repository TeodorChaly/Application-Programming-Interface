from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DP_HOST = "localhost"
DP_PORT = 5432
DP_USER = "postgres"
DP_PASSWORD = "postgres"
DP_NAME = "postgres"

DATABASE_URL = f"postgresql+asyncpg://{DP_USER}:{DP_PASSWORD}@{DP_HOST}:{DP_PORT}/{DP_NAME}"

engine = create_async_engine(DATABASE_URL)

async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):
    pass
