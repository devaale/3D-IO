from typing import *
from app.common.errors.camera import CameraError
from app.hardware.camera.base import CameraReader
from app.common.models.camera_data import CameraData


class CameraService:
    SAMPLE_COUNT = 5

    def __init__(self, camera_reader: CameraReader):
        self._camera_reader = camera_reader

    async def start(self):
        try:
            return await self._camera_reader.connect()
        except Exception as error:
            print(f"Camera connect error: {error}")

    async def read(self) -> CameraData:
        depth_frames = []
        color_frames = []

        try:
            depth_frames, color_frames = await self._camera_reader.read(
                self.SAMPLE_COUNT
            )
        except Exception as error:
            print(f"Camera read error: {error}")

        intrinsics = await self._camera_reader.intrinsics()

        return CameraData(depth_frames, color_frames, intrinsics)

    async def stop(self):
        try:
            return not await self._camera_reader.disconnect()
        except Exception as error:
            print(f"Camera disconnect error: {error}")
