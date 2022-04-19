from typing import List
from sqlmodel import select
from app.models.plc_block import PlcBlock, PlcBlockCreate
from app.database.session import ScopedSession


class CRUDPlcBlock:
    def __init__(self) -> None:
        pass

    async def get(self, id: int) -> PlcBlock:
        async with ScopedSession() as session:
            return await session.get(PlcBlock, id)

    async def get_all(self) -> List[PlcBlock]:
        async with ScopedSession() as session:
            query = select(PlcBlock)
            result = await session.execute(query)
            return result.scalars().all()

    async def add(self, data: PlcBlockCreate) -> PlcBlock:
        async with ScopedSession() as session:
            obj = PlcBlock.from_orm(data)
            session.add(obj)
            await session.commit()
            await session.refresh(obj)
            return obj

    async def delete(self, data: PlcBlock) -> PlcBlock:
        async with ScopedSession() as session:
            obj = await session.delete(data)
            await session.commit()
            return obj
