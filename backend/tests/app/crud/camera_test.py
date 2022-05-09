# from backend.app.models.camera import CameraCreate
# from backend.app.crud.camera import CameraCRUD
# import pytest

# from sqlmodel import SQLModel

# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession


# @pytest.mark.asyncio
# async def test_camera_create():
#     DATABASE_URL = "sqlite+aiosqlite:///./test_database.db"
#     engine = create_async_engine(DATABASE_URL, echo=True, future=True)
#     ScopedSession = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

#     async with engine.begin() as conn:
#         await conn.run_sync(SQLModel.metadata.create_all)

#     async with ScopedSession() as session:
#         expected = CameraCreate()
#         result = await CameraCRUD().add(data=expected, session=session)

#     assert result.serial_num == expected.serial_num


# @pytest.mark.asyncio
# async def test_camera_get():
#     DATABASE_URL = "sqlite+aiosqlite:///./test_database.db"
#     engine = create_async_engine(DATABASE_URL, echo=True, future=True)
#     ScopedSession = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

#     async with engine.begin() as conn:
#         await conn.run_sync(SQLModel.metadata.create_all)

#     expected = CameraCreate()

#     async with ScopedSession() as session:
#         _ = await CameraCRUD().add(data=expected, session=session)
#         result = await CameraCRUD().get(session=session)
#     assert result.serial_num == expected.serial_num
