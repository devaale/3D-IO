from app.services.procesing import ProcessingService
from app.processing.pipelines.default import DefaultProcessingPipeline
from app.models.product import ProductCreate
from app.database.session import connect_test_db, ScopedSessionTest

import pytest


@pytest.mark.asyncio
async def test_processing_error_no_input():
    service = ProcessingService(session_proxy=None, processing_pipeline=None)
    with pytest.raises(Exception):
        _ = await service.process(None)


@pytest.mark.asyncio
async def test_processing_error_during_processing_steps(test_cloud):
    await connect_test_db()

    async with ScopedSessionTest() as session:
        session_proxy = TrySessionProxy(session=session)
        service = ProcessingService(
            session_proxy=session_proxy, processing_pipeline=None
        )
        with pytest.raises(Exception):
            _ = await service.process(test_cloud)


@pytest.mark.asyncio
async def test_processing_configure_true():
    service = ProcessingService(session_proxy=None, processing_pipeline=None)
    configured = await service.configure(ProductCreate(), DefaultProcessingPipeline())
    assert configured is True


@pytest.mark.asyncio
async def test_processing_configure_false():
    service = ProcessingService(session_proxy=None, processing_pipeline=None)
    configured = await service.configure(None, None)
    assert configured is False


class TrySessionProxy:
    def __init__(self, session) -> None:
        self._session = session

    def get(self):
        return self._session
