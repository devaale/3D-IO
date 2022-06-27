from typing import List
from sqlmodel import select
from app.models.plc_block import PlcBlock, PlcBlockCreate
from sqlalchemy.ext.asyncio import AsyncSession


class CRUDPlcBlock:
    def __init__(self) -> None:
        pass

    async def get(self, id: int, session: AsyncSession) -> PlcBlock:
        return await session.get(PlcBlock, id)

    async def get_all(self, session: AsyncSession) -> List[PlcBlock]:

        query = select(PlcBlock)
        result = await session.execute(query)
        return result.scalars().all()

    async def add(self, data: PlcBlockCreate, session: AsyncSession) -> PlcBlock:
        obj = PlcBlock.from_orm(data)
        session.add(obj)
        await session.commit()
        await session.refresh(obj)
        return obj

    async def delete(self, data: PlcBlock, session: AsyncSession) -> PlcBlock:
        obj = await session.delete(data)
        await session.commit()
        return obj
