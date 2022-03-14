from typing import List
from fastapi import HTTPException

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.plc_block import PlcBlock, PlcBlockCreate

class CRUDPlcBlock:
    
    async def get_all_by_plc(session: AsyncSession, plc_id: int) -> List[PlcBlock]:
        query = select(PlcBlock).where(PlcBlock.plc_id == plc_id)
        data = await session.execute(query)
        return data.scalars().all()
    
    async def add(session: AsyncSession, setting: PlcBlockCreate) -> PlcBlock:
        data = PlcBlock.from_orm(setting)
        session.add(data)
        await session.commit()
        await session.refresh(data)
        return data
    
    async def delete(session: AsyncSession, id: int) -> PlcBlock:
        data = await session.get(PlcBlock, id)

        if not data:
            raise HTTPException(status_code=404, detail="Plc not found")
        
        await session.delete(data)
        await session.commit()
        return data