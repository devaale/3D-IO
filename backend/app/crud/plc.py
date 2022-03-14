from fastapi import HTTPException
from typing import List

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.plc import Plc, PlcCreate

class CRUDPlc:
    
    async def get(session: AsyncSession) -> Plc:
        query = select(Plc).where(Plc.id == 1)
        data = await session.execute(query)
        if not data:
            raise HTTPException(status_code=404, detail="Plc not found")
            
        return data.scalars().first()
    
    async def add(session: AsyncSession, setting: PlcCreate) -> Plc:
        data = Plc.from_orm(setting)
        session.add(data)
        await session.commit()
        await session.refresh(data)
        return data
    
    async def delete(session: AsyncSession, id: int) -> Plc:
        data = await session.get(Plc, id)

        if not data:
            raise HTTPException(status_code=404, detail="Plc not found")
        
        await session.delete(data)
        await session.commit()
        return data