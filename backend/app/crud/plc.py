from app.models.plc import Plc, PlcCreate

from sqlalchemy.ext.asyncio import AsyncSession


class CRUDPlc:
    async def get(session: AsyncSession, id: int = 1) -> Plc:
        return await session.get(Plc, id)

    async def add(session: AsyncSession, data: PlcCreate) -> Plc:
        entity = Plc.from_orm(data)
        session.add(entity)
        await session.commit()
        await session.refresh(entity)
        return entity

    async def delete(session: AsyncSession, data: Plc) -> Plc:
        entity = await session.delete(data)
        await session.commit()
        return entity

    async def exists(session: AsyncSession, id: int = 1) -> bool:
        return await session.get(Plc, id) is not None
