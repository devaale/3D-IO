import asyncio
import numpy as np
from app.services.camera import CameraService
from app.services.visualization import VisualizationService

from app.common.interfaces.camera.reader_factory import CameraReaderFactory
from app.services.detection import DetectionService
from app.services.procesing import ProcessingService
from app.services.product import CurrentProductService
from app.common.interfaces.database.session_proxy import SessionProxy
from app.services.settings import SettingsService
from app.services.result import ResultService
from app.crud.camera import CameraCRUD
from app.common.interfaces.processing.pipeline_factory import ProcessingPipelineFactory
from app.services.result_viz import VisualizerResult


class CoreService:
    def __init__(
        self,
        session: SessionProxy,
        camera_reader_factory: CameraReaderFactory,
        processing_pipeline_factory: ProcessingPipelineFactory,
    ) -> None:
        self._session_proxy = session

        self._camera = None
        self._camera_reader_factory = camera_reader_factory
        self._camera_service = CameraService()

        self._processing_pipeline_factory = processing_pipeline_factory
        self._processing_service = ProcessingService(session_proxy=self._session_proxy)

        self._settings_service = SettingsService(session_proxy=self._session_proxy)
        self._product_service = CurrentProductService(session_proxy=self._session_proxy)

        self._visualization_service = None

        self._detection_service = None

        self._visualizer_result = VisualizerResult()

    async def configure(self):
        await self.configure_camera_service()

        await self.configure_processing_service()

        await self.configure_detection_service()

        self.visualization_service = VisualizationService()

    async def configure_camera_service(self):
        session_scoped = self._session_proxy.get()

        async with session_scoped as session:
            self._camera = await CameraCRUD().get(session=session)

        camera_reader = self._camera_reader_factory.create(
            self._camera.type,
            self._camera.model,
            self._camera.width,
            self._camera.height,
            self._camera.fps,
            self._camera.serial_num,
        )

        await self._camera_service.configure(camera_reader)

        print("[CORE] Configured camera service")

    async def configure_processing_service(self):

        current_product = await self._product_service.get_current()

        processing_pipeline = self._processing_pipeline_factory.create(
            current_product.model
        )

        await self._processing_service.configure(current_product, processing_pipeline)

        print("[CORE] Configured processing service")

    async def configure_detection_service(self):
        self._detection_service = DetectionService(
            SettingsService(session_proxy=self._session_proxy),
            CurrentProductService(session_proxy=self._session_proxy),
            ResultService(self._session_proxy),
        )

        print("[CORE] Configured detection service")

    async def start(self):
        await self.configure()

        result = {0: True, 1: False, 2: True}

        try:
            await self._camera_service.start()

            self.visualization_service.start()

            self._visualizer_result.create()

            while True:
                data = None

                try:
                    data = await self._camera_service.read()
                except Exception as error:
                    print(error)
                    continue

                clusters, ground_plane = await self._processing_service.process(data)

                print("PROCESSED")

                cloud = await self._detection_service.detect(clusters, ground_plane)

                print("DETECTED")

                await self.visualize(cloud, data.get_color_data()[0])

                self._visualizer_result.update(result)

                await asyncio.sleep(0.001)

        except Exception as error:
            print(f"Error occured: {error}")
        finally:
            await self._camera_service.stop()
            self.visualization_service.stop()

    async def visualize(self, cloud, color_frame):
        self.visualization_service.visualize_cloud(cloud)

        self.visualization_service.visualize_color_frame(color_frame)
