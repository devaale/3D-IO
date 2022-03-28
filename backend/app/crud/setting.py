from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.setting import Setting, SettingCreate


class CRUDSetting:
    async def get(session: AsyncSession, id: int = 1) -> Setting:
        return await session.get(Setting, id)

    async def get_all(session: AsyncSession) -> List[Setting]:
        query = select(Setting)
        result = await session.execute(query)
        return result.scalars().all()

    async def add(session: AsyncSession, data: SettingCreate) -> Setting:
        obj = Setting.from_orm(data)
        session.add(obj)
        await session.commit()
        await session.refresh(obj)
        return obj

    async def delete(session: AsyncSession, data: Setting) -> Setting:
        obj = await session.delete(data)
        await session.commit()
        return obj

    async def exists(session: AsyncSession, id: int = 1) -> bool:
        return await session.get(Setting, id) is not None
