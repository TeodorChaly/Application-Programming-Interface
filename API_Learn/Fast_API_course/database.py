
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_async_engine(
    "sqlite+aiosqlite:///API_Learn/Fast_API_course/tasks.db"
)
new_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
