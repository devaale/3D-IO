import asyncio
from app.services.camera import CameraService


class ServiceManager:
    def __init__(self, camera_service: CameraService) -> None:
        self._created = False
        self._camera_task = None
        self._camera_service = camera_service

    async def camera_start(self):
        if not self._created:
            self._camera_task = asyncio.create_task(self._camera_service.run())
            self._created = True

    async def camera_detect(self):
        await self._camera_service.set_manual_detect()
