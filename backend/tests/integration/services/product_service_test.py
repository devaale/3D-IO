from app.database.session import connect_test_db, ScopedSessionTest
import pytest
from app.models.product import ProductCreate
from app.services.product import CurrentProductService
from app.crud.product import ProductCRUD


@pytest.mark.asyncio
async def test_product_service_get_current():
    await connect_test_db()
    async with ScopedSessionTest() as session:
        data = ProductCreate(current=True)
        _ = await ProductCRUD().create(data=data, session=session)
        proxy = TrySessionProxy(session=session)
        service = CurrentProductService(proxy)
        product = await service.get_current()
        assert product.model == data.model


class TrySessionProxy:
    def __init__(self, session) -> None:
        self._session = session

    def get(self):
        return self._session
