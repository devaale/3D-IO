from typing import List
from sqlmodel import select
from app.models.region import RegionModel
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.region import RegionDetected


class RegionModelCRUD:
    def __init__(self) -> None:
        pass

    async def get(self, id: int, session: AsyncSession) -> RegionModel:
        return await session.get(RegionModel, id)

    async def get_all(self, session: AsyncSession) -> List[RegionModel]:
        query = select(RegionModel)
        result = await session.execute(query)
        return result.scalars().all()

    async def get_all_by_position_model(
        self, position_model_id: int, session: AsyncSession
    ) -> List[RegionModel]:
        query = select(RegionModel).where(
            RegionModel.position_model_id == position_model_id
        )
        result = await session.execute(query)

        return result.scalars().all()

    async def add(self, data: RegionDetected, session: AsyncSession) -> RegionModel:
        obj = RegionModel.from_orm(data)
        session.add(obj)
        await session.commit()
        await session.refresh(obj)
        return obj

    async def delete(self, data: RegionModel, session: AsyncSession) -> RegionModel:
        obj = await session.delete(data)
        await session.commit()
        return obj

    async def find_by_position_and_position_model(
        self, position: str, position_model_id: int, session: AsyncSession
    ) -> RegionModel:
        print(
            f"positionposition: {position} ---- position_model_idposition_model_id: {position_model_id} ---- "
        )
        query = select(RegionModel).where(
            RegionModel.position == position,
            RegionModel.position_model_id == position_model_id,
        )

        results = await session.execute(query)

        try:
            return results.scalars().all()[0]
        except Exception as error:
            return None

    async def update(self, data: RegionModel, session: AsyncSession) -> RegionModel:
        obj = await session.get(RegionModel, data.id)

        obj.depth_mean = data.depth_mean

        session.add(obj)

        await session.commit()

        await session.refresh(obj)

        return obj
