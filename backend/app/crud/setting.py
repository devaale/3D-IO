from typing import List
from sqlalchemy import select
from app.database.session import ScopedSession
from app.models.setting import Setting, SettingCreate


class CRUDSetting:
    def __init__(self) -> None:
        pass

    async def get(self, id: int = 1) -> Setting:
        async with ScopedSession() as session:
            return await session.get(Setting, id)

    async def get_all(self) -> List[Setting]:
        async with ScopedSession() as session:
            query = select(Setting)
            result = await session.execute(query)
            return result.scalars().all()

    async def add(self, data: SettingCreate) -> Setting:
        async with ScopedSession() as session:
            obj = Setting.from_orm(data)
            session.add(obj)
            await session.commit()
            await session.refresh(obj)
            return obj

    async def delete(self, data: Setting) -> Setting:
        async with ScopedSession() as session:
            obj = await session.delete(data)
            await session.commit()
            return obj

    async def update_value(self, id: int, value: float):
        async with ScopedSession() as session:
            obj = await session.get(Setting, id)
            obj.value = float(value)
            session.add(obj)
            await session.commit()
            await session.refresh(obj)
            return obj

    async def exists(self, id: int = 1) -> bool:
        async with ScopedSession() as session:
            return await session.get(Setting, id) is not None
