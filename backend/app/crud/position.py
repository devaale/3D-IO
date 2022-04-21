from typing import List
from sqlmodel import select
from app.models.position import PositionModel, PositionModelCreate
from app.database.session import ScopedSession


class PositionModelCRUD:
    def __init__(self) -> None:
        pass

    async def get(self, id: int) -> PositionModel:
        async with ScopedSession() as session:
            return await session.get(PositionModel, id)

    async def get_all(self) -> List[PositionModel]:
        async with ScopedSession() as session:
            query = select(PositionModel)
            result = await session.execute(query)
            return result.scalars().all()

    async def add(self, data: PositionModelCreate) -> PositionModel:
        async with ScopedSession() as session:
            obj = PositionModel.from_orm(data)
            session.add(obj)
            await session.commit()
            await session.refresh(obj)
            return obj

    async def delete(self, data: PositionModel) -> PositionModel:
        async with ScopedSession() as session:
            obj = await session.delete(data)
            await session.commit()
            return obj

    async def find_by_position_and_product(self, row: int, col: int, product_id: int):
        async with ScopedSession() as session:
            query = select(PositionModel).where(
                PositionModel.row == row
                and PositionModel.col == col
                and PositionModel.product_id == product_id
            )
            result = await session.execute(query)

            return result
