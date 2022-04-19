from typing import List
from sqlmodel import select
from app.models.region import RegionModel, RegionModelCreate
from app.database.session import ScopedSession


class RegionModelCRUD:
    def __init__(self) -> None:
        pass

    async def get(self, id: int) -> RegionModel:
        async with ScopedSession() as session:
            return await session.get(RegionModel, id)

    async def get_all(self) -> List[RegionModel]:
        async with ScopedSession() as session:
            query = select(RegionModel)
            result = await session.execute(query)
            return result.scalars().all()

    async def add(self, data: RegionModelCreate) -> RegionModel:
        async with ScopedSession() as session:
            obj = RegionModel.from_orm(data)
            session.add(obj)
            await session.commit()
            await session.refresh(obj)
            return obj

    async def delete(self, data: RegionModel) -> RegionModel:
        async with ScopedSession() as session:
            obj = await session.delete(data)
            await session.commit()
            return obj
