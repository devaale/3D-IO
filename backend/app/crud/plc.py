from app.models.plc import Plc, PlcCreate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select


class CRUDPlc:
    def __init__(self) -> None:
        pass

    async def get(self, id: int, session: AsyncSession) -> Plc:
        return await session.get(Plc, 1)

    async def add(self, data: PlcCreate, session: AsyncSession) -> Plc:
        obj = Plc.from_orm(data)
        session.add(obj)
        await session.commit()
        await session.refresh(obj)
        return obj

    async def delete(self, data: Plc, session: AsyncSession) -> Plc:
        delete = await session.get(Plc, data.id)
        obj = await session.delete(delete)
        await session.commit()
        return obj

    async def exists(self, id: int, session: AsyncSession) -> bool:
        return await session.get(Plc, 1) is not None
