from sqlmodel import SQLModel

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession


DATABASE_URL = "sqlite+aiosqlite:///./database.db"
engine = create_async_engine(DATABASE_URL, echo=True, future=True)
ScopedSession = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


DATABASE_URL_TEST = "sqlite+aiosqlite:///./test.db"
engine_test = create_async_engine(DATABASE_URL_TEST, echo=True, future=True)
ScopedSessionTest = sessionmaker(
    engine_test, class_=AsyncSession, expire_on_commit=False
)


async def connect_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)


async def connect_test_db():
    async with engine_test.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)


async def disconnect_db():
    await engine.dispose()


async def get_session() -> AsyncSession:
    async with ScopedSession() as session:
        yield session
