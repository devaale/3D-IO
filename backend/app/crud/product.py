from typing import List
from sqlmodel import select
from app.models.product import Product, ProductCreate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel.sql.expression import Select, SelectOfScalar

SelectOfScalar.inherit_cache = True  # type: ignore
Select.inherit_cache = True  # type: ignore


class ProductCRUD:
    def __init__(self) -> None:
        pass

    async def get(self, id: int, session: AsyncSession) -> Product:
        return await session.get(Product, id)

    async def get_all(self, session: AsyncSession) -> List[Product]:
        query = select(Product)
        result = await session.execute(query)
        return result.scalars().all()

    async def get_current(self, session: AsyncSession) -> List[Product]:
        query = select(Product).where(Product.current == True)
        result = await session.execute(query)
        return result.scalars().one()

    async def create(self, data: ProductCreate, session: AsyncSession) -> Product:
        obj = Product.from_orm(data)
        session.add(obj)
        await session.commit()
        await session.refresh(obj)
        return obj

    async def delete(self, data: Product, session: AsyncSession) -> Product:
        delete = await session.get(Product, data.id)
        obj = await session.delete(delete)
        await session.commit()
        return obj
