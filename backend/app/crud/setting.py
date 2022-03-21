from typing import List

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.setting import Setting, SettingCreate


class CRUDSetting:
    async def get(session: AsyncSession, id: int = 1) -> Setting:
        return await session.get(Setting, id)

    async def get_all(session: AsyncSession) -> List[Setting]:
        query = select(Setting).all()
        result = await session.execute(query)
        return result.scalars().all()

    async def add(session: AsyncSession, data: SettingCreate) -> Setting:
        entity = Setting.from_orm(data)
        session.add(entity)
        await session.commit()
        await session.refresh(entity)
        return entity

    async def delete(session: AsyncSession, data: Setting) -> Setting:
        entity = await session.delete(data)
        await session.commit()
        return entity

    async def exists(session: AsyncSession, id: int = 1) -> bool:
        return await session.get(Setting, id) is not None
