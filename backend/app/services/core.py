import asyncio

from app.services.camera import CameraService
from app.services.visualization import VisualizationService

from app.hardware.camera.factory import CameraReaderFactory
from app.common.models.camera_data import CameraData
from app.services.detection import DetectionService
from app.services.procesing import ProcessingService
from app.services.product import CurrentProductService
from app.common.interfaces.session_proxy import SessionProxy
from app.services.settings import SettingsService
from app.services.result import ResultService
from app.crud.camera import CameraCRUD


class CoreService:
    def __init__(self, session: SessionProxy) -> None:
        self._session_proxy = session
        self._settings_service = None

        self._camera = None
        self._product_service = None
        self.camera_service = None
        self.visualization_service = None

        self.detection_service = None
        self.processing_pipeline = None

    async def configure(self):
        self._settings_service = SettingsService(session_proxy=self._session_proxy)

        self._product_service = CurrentProductService(session_proxy=self._session_proxy)

        await self.configure_camera()

        await self.configure_processing()

        await self.configure_detection()

        self.visualization_service = VisualizationService()

    async def configure_camera(self):
        session_scoped = self._session_proxy.get()

        async with session_scoped as session:
            self._camera = await CameraCRUD().get(session=session)

        camera_reader = CameraReaderFactory.create(
            self._camera.camera_type,
            self._camera.width,
            self._camera.height,
            self._camera.fps,
            self._camera.serial_num,
        )

        self.camera_service = CameraService(camera_reader)

    async def configure_processing(self):
        self.processing_service = ProcessingService()

        current_product = await self._product_service.get_current()

        await self.processing_service.configure(
            SettingsService(session_proxy=self._session_proxy), current_product
        )

    async def configure_detection(self):
        self.detection_service = DetectionService(
            SettingsService(session_proxy=self._session_proxy),
            CurrentProductService(session_proxy=self._session_proxy),
            ResultService(self._session_proxy),
        )

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
