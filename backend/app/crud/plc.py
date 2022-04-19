from app.models.plc import Plc, PlcCreate
from app.database.session import ScopedSession


class CRUDPlc:
    def __init__(self) -> None:
        pass

    async def get(self, id: int = 1) -> Plc:
        async with ScopedSession() as session:
            return await session.get(Plc, id)

    async def add(self, data: PlcCreate) -> Plc:
        async with ScopedSession() as session:
            obj = Plc.from_orm(data)
            session.add(obj)
            await session.commit()
            await session.refresh(obj)
            return obj

    async def delete(self, data: Plc) -> Plc:
        async with ScopedSession() as session:
            obj = await session.delete(data)
            await session.commit()
            return obj

    async def exists(self, id: int = 1) -> bool:
        async with ScopedSession() as session:
            return await session.get(Plc, id) is not None
