from typing import List
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.setting import Setting, SettingCreate

from sqlmodel.sql.expression import Select, SelectOfScalar

SelectOfScalar.inherit_cache = True  # type: ignore
Select.inherit_cache = True  # type: ignore


class CRUDSetting:
    def __init__(self) -> None:
        pass

    async def get(self, id: int, session: AsyncSession) -> Setting:
        return await session.get(Setting, id)

    async def get_all(self, session: AsyncSession) -> List[Setting]:
        query = select(Setting)
        result = await session.execute(query)
        return result.scalars().all()

    async def add(self, data: SettingCreate, session: AsyncSession) -> Setting:
        obj = Setting.from_orm(data)
        session.add(obj)
        await session.commit()
        await session.refresh(obj)
        return obj

    async def delete(self, data: Setting, session: AsyncSession) -> Setting:
        delete = await session.get(Setting, data.id)
        obj = await session.delete(delete)
        await session.commit()
        return obj

    async def update_value(self, id: int, value: float, session: AsyncSession):
        obj = await session.get(Setting, id)
        obj.value = float(value)
        session.add(obj)
        await session.commit()
        await session.refresh(obj)
        return obj

    async def exists(self, id: int, session: AsyncSession) -> bool:
        return await session.get(Setting, id) is not None
