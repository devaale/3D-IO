from typing import *
from app.common.interfaces.camera.output import CameraOutput
from app.common.interfaces.camera.reader import CameraReader
from app.common.errors.camera import CameraError


class CameraService:
    SAMPLE_COUNT = 5

    def __init__(self, camera_reader: CameraReader = None):
        self._camera_reader = camera_reader

    async def start(self):
        try:
            return await self._camera_reader.connect()
        except Exception as error:
            raise CameraError("Failed to start")

    async def configure(self, camera_reader: CameraReader) -> bool:
        self._camera_reader = camera_reader
        return self._camera_reader is not None

    async def read(self) -> CameraOutput:
        try:
            camera_data = await self._camera_reader.read(self.SAMPLE_COUNT)
        except Exception as error:
            raise CameraError("Failed to read")

        return camera_data

    async def stop(self):
        try:
            return not await self._camera_reader.disconnect()
        except Exception as error:
            raise CameraError("Failed to stop")
