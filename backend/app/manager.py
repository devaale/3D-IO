import asyncio
from app.services.core import CoreService
from app.database.sql_session import AsyncSQLSessionProxy
from hardware.camera.factory import AbstractCameraReaderFactory
from app.processing.factory import PointCloudProcessingPipelineFactory


class ServiceManager:
    def __init__(self) -> None:
        self._created = False
        self._core_task = None

        self._core_service = CoreService(
            AsyncSQLSessionProxy(),
            AbstractCameraReaderFactory(),
            PointCloudProcessingPipelineFactory(),
        )

    async def camera_start(self):
        if not self._created:
            self._core_task = asyncio.create_task(self._core_service.start())
            self._created = True

    async def set_product_algorithm(self, algorithm_type: str):
        self._core_service.set_processing_algorithm(algorithm_type)

    async def detect(self):
        await self._core_service.set_detect()

    async def train(self):
        await self._core_service.set_train()
