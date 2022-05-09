# from backend.app.models.plc import PlcCreate
# from backend.app.crud.plc import CRUDPlc
# import pytest

# from sqlmodel import SQLModel

# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession


# @pytest.mark.asyncio
# async def test_plc_create():
#     DATABASE_URL = "sqlite+aiosqlite:///./test_database.db"
#     engine = create_async_engine(DATABASE_URL, echo=True, future=True)
#     ScopedSession = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

#     async with engine.begin() as conn:
#         await conn.run_sync(SQLModel.metadata.create_all)

#     async with ScopedSession() as session:
#         expected = PlcCreate()
#         result = await CRUDPlc().add(data=expected, session=session)

#     assert result.ip == expected.ip


# @pytest.mark.asyncio
# async def test_plc_get():
#     DATABASE_URL = "sqlite+aiosqlite:///./test_database.db"
#     engine = create_async_engine(DATABASE_URL, echo=True, future=True)
#     ScopedSession = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

#     async with engine.begin() as conn:
#         await conn.run_sync(SQLModel.metadata.create_all)

#     expected = PlcCreate()

#     async with ScopedSession() as session:
#         _ = await CRUDPlc().add(data=expected, session=session)
#         result = await CRUDPlc().get(session=session)
#     assert result.ip == expected.ip
