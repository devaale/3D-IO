from typing import List

from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.plc_block import PlcBlock, PlcBlockCreate


class CRUDPlcBlock:
    async def get(session: AsyncSession, id: int) -> PlcBlock:
        return await session.get(PlcBlock, id)

    async def get_all(session: AsyncSession) -> List[PlcBlock]:
        query = select(PlcBlock)
        result = await session.execute(query)
        return result.scalars().all()

    async def add(session: AsyncSession, data: PlcBlockCreate) -> PlcBlock:
        obj = PlcBlock.from_orm(data)
        session.add(obj)
        await session.commit()
        await session.refresh(obj)
        return obj

    async def delete(session: AsyncSession, data: PlcBlock) -> PlcBlock:
        obj = await session.delete(data)
        await session.commit()
        return obj
