from app.models.plc import Plc, PlcCreate
from sqlalchemy.ext.asyncio import AsyncSession


class CRUDPlc:
    async def get(session: AsyncSession, id: int = 1) -> Plc:
        return await session.get(Plc, id)

    async def add(session: AsyncSession, data: PlcCreate) -> Plc:
        obj = Plc.from_orm(data)
        session.add(obj)
        await session.commit()
        await session.refresh(obj)
        return obj

    async def delete(session: AsyncSession, data: Plc) -> Plc:
        obj = await session.delete(data)
        await session.commit()
        return obj

    async def exists(session: AsyncSession, id: int = 1) -> bool:
        return await session.get(Plc, id) is not None
