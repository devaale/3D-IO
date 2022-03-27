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
        entity = PlcBlock.from_orm(data)
        session.add(entity)
        await session.commit()
        await session.refresh(entity)
        return entity

    async def delete(session: AsyncSession, data: PlcBlock) -> PlcBlock:
        entity = await session.delete(data)
        await session.commit()
        return entity
