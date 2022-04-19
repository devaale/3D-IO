from typing import List
from sqlmodel import select
from app.models.product import Product, ProductCreate
from app.database.session import ScopedSession


class ProductCRUD:
    def __init__(self) -> None:
        pass

    async def get(self, id: int) -> Product:
        async with ScopedSession() as session:
            return await session.get(Product, id)

    async def get_all(self) -> List[Product]:
        async with ScopedSession() as session:
            query = select(Product)
            result = await session.execute(query)
            return result.scalars().all()

    async def get_current(self) -> List[Product]:
        async with ScopedSession() as session:
            query = select(Product).where(Product.current == True)
            result = await session.execute(query)
            return result.scalars().one()

    async def create(self, data: ProductCreate) -> Product:
        async with ScopedSession() as session:
            obj = Product.from_orm(data)
            session.add(obj)
            await session.commit()
            await session.refresh(obj)
            return obj

    async def delete(self, data: Product) -> Product:
        async with ScopedSession() as session:
            obj = await session.delete(data)
            await session.commit()
            return obj
