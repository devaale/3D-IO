from app.database.session import connect_test_db, ScopedSessionTest
import pytest
from app.models.product import ProductCreate
from app.services.model import ModelService
from app.crud.product import ProductCRUD


@pytest.mark.asyncio
async def test_model_service_get_position_model_none():
    await connect_test_db()
    async with ScopedSessionTest() as session:
        data = ProductCreate(current=True)
        _ = await ProductCRUD().create(data=data, session=session)
        proxy = TrySessionProxy(session=session)
        service = ModelService(proxy)
        position_model = await service.get_position_model(0, 0, 0)

        assert position_model is None


@pytest.mark.asyncio
async def test_model_service_get_region_model_none():
    await connect_test_db()
    async with ScopedSessionTest() as session:
        data = ProductCreate(current=True)
        _ = await ProductCRUD().create(data=data, session=session)
        proxy = TrySessionProxy(session=session)
        service = ModelService(proxy)
        region_model = await service.get_region_model("", 0)

        assert region_model is None


class TrySessionProxy:
    def __init__(self, session) -> None:
        self._session = session

    def get(self):
        return self._session
