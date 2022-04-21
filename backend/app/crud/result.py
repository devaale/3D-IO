from typing import List
from app.models.result import Result
from app.models.result import ResultCreate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select


class ResultCRUD:
    def __init__(self) -> None:
        pass

    async def get(self, id: int, session: AsyncSession) -> Result:
            return await session.get(Result, id)

    async def get_all(self, session: AsyncSession) -> List[Result]:
            query = select(Result)
            result = await session.execute(query)
            return result.scalars().all()

    async def add(self, data: ResultCreate, session: AsyncSession) -> Result:
            obj = Result.from_orm(data)
            session.add(obj)
            await session.commit()
            await session.refresh(obj)
            return obj
