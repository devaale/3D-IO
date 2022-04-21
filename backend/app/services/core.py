import asyncio

from app.services.camera import CameraService
from app.services.visualization import VisualizationService

from app.hardware.camera.factory import CameraReaderFactory
from app.common.models.camera_data import CameraData
from app.services.detection import DetectionService
from app.services.procesing import ProcessingService
from app.services.product import CurrentProductService
from app.services.result import ResultService


class CoreService:
    def __init__(self) -> None:
        self.camera_service = None
        self.detection_service = None
        self.processing_pipeline = None
        self.visualization_service = None
        self.result_service = None
        self.product_service = CurrentProductService()

    async def configure(self):
        camera_reader = CameraReaderFactory.create(
            "REAL_SENSE", 848, 480, 30, "823112061406"
        )
        self.camera_service = CameraService(camera_reader)

        self.visualization_service = VisualizationService()

        self.detection_service = DetectionService()

        self.processing_service = ProcessingService()

        current_product = await self.product_service.get_current()

        await self.processing_service.configure(current_product)

    async def start(self):
        await self.configure()

        try:
            await self.camera_service.start()

            self.visualization_service.start()

            while True:
                camera_data = CameraData()

                try:
                    camera_data = await self.camera_service.read()
                except Exception as error:
                    print(error)
                    continue

                clusters = await self.processing_service.process(camera_data)

                cloud, _ = await self.detection_service.detect(clusters)

                await self.visualize(cloud, camera_data.color_data[0])

                await asyncio.sleep(0.001)

        except Exception as error:
            print(f"Error occured: {error}")
        finally:
            await self.camera_service.stop()
            self.visualization_service.stop()

    async def visualize(self, cloud, color_frame):
        self.visualization_service.visualize_cloud(cloud)

        self.visualization_service.visualize_color_frame(color_frame)
