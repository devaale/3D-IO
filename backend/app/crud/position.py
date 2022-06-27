from typing import List
from sqlmodel import select
from app.models.position import PositionModel
from app.models.position import PositionDetected
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel.sql.expression import Select, SelectOfScalar

SelectOfScalar.inherit_cache = True  # type: ignore
Select.inherit_cache = True  # type: ignore


class PositionModelCRUD:
    def __init__(self) -> None:
        pass

    async def get(self, id: int, session: AsyncSession) -> PositionModel:
        return await session.get(PositionModel, id)

    async def get_all(self, session: AsyncSession) -> List[PositionModel]:
        query = select(PositionModel)
        result = await session.execute(query)
        return result.scalars().all()

    async def add(self, data: PositionDetected, session: AsyncSession) -> PositionModel:
        obj = PositionModel.from_orm(data)
        session.add(obj)
        await session.commit()
        await session.refresh(obj)
        return obj

    async def delete(self, data: PositionModel, session: AsyncSession) -> PositionModel:
        delete = await session.get(PositionModel, data.id)
        obj = await session.delete(delete)
        await session.commit()
        return obj

    async def find_by_position_and_product(
        self, row: int, col: int, product_id: int, session: AsyncSession
    ):
        query = select(PositionModel).where(
            PositionModel.row == row,
            PositionModel.col == col,
            PositionModel.product_id == product_id,
        )

        results = await session.execute(query)

        try:
            return results.scalars().all()[0]
        except Exception as error:
            return None

    async def update(self, data: PositionModel, session: AsyncSession) -> PositionModel:
        obj = await session.get(PositionModel, data.id)

        obj.plane_angle = data.plane_angle

        session.add(obj)

        await session.commit()

        await session.refresh(obj)

        return obj
