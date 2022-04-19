import asyncio
from asyncio import Event

from typing import *

from app.common.errors.camera import CameraError
from app.hardware.camera.reader import CameraReader
from app.services.visualization import Visualizer
from app.services.detection import DetectionService
from app.processing.pipeline import ProcessingPipeline


class CameraService:
    SAMPLE_COUNT = 5

    def __init__(self):
        self._trigger = Event()
        self._visualizer = Visualizer()

        self._detection_service = DetectionService()
        self._processing_pipeline = ProcessingPipeline()

        self._camera_reader = CameraReader(848, 480, 30, "823112061406")

    async def set_manual_reference(self):
        self._trigger.set()

    async def set_manual_detect(self):
        self._trigger.set()

    async def connect(self):
        try:
            return await self._camera_reader.connect()
        except CameraError as error:
            print(error)

    async def disconnect(self):
        try:
            return not await self._camera_reader.disconnect()
        except CameraError as error:
            print(error)

    async def run(self):
        await self.connect()

        self._visualizer.create_window()

        try:
            while True:
                if self._trigger.is_set():
                    depth_frames = []

                    try:
                        depth_frames, _ = await self._camera_reader.read(
                            self.SAMPLE_COUNT
                        )
                    except CameraError as error:
                        print(error)
                        continue

                    intrinsics = await self._camera_reader.intrinsics()

                    clusters = await self._processing_pipeline.process(
                        depth_frames, intrinsics
                    )

                    cloud, results = await self._detection_service.detect(clusters)

                    self._trigger.clear()

                await self.visualize()

                await asyncio.sleep(0.001)
        finally:
            await self.disconnect()

    async def visualize(self):
        depth_frames, color_frames = await self._camera_reader.read(1)

        intrinsics = await self._camera_reader.intrinsics()

        clusters = await self._processing_pipeline.process(depth_frames, intrinsics)

        cloud, _ = await self._detection_service.detect(clusters)

        self._visualizer.visualize_cloud(cloud)

        self._visualizer.visualize_color_frame(color_frames[0])

    async def stop(self):
        self._camera_reader.disconnect()
