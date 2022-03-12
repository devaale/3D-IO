from fastapi import HTTPException
from typing import List

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.setting import Setting, SettingCreate

class CRUDSetting:
    
    async def get_all(session: AsyncSession) -> List[Setting]:
        query = select(Setting)
        result = await session.execute(query)
        return result.scalars().all()
    
    async def add(session: AsyncSession, setting: SettingCreate) -> Setting:
        data = Setting.from_orm(setting)
        session.add(data)
        await session.commit()
        await session.refresh(data)
        return data
    
    async def delete(session: AsyncSession, id: int) -> Setting:
        data = await session.get(Setting, id)

        if not data:
            raise HTTPException(status_code=404, detail="Setting not found")
        
        await session.delete(data)
        await session.commit()
        return data