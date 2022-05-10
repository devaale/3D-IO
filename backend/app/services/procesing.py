from app.models.product import Product
from app.common.interfaces.camera.output import CameraOutput
from app.common.interfaces.processing.pipeline import ProcessingPipeline
from app.common.interfaces.database.session_proxy import SessionProxy
from app.services.settings import SettingsService
from app.common.errors.processing import ProcessingError


class ProcessingService:
    def __init__(
        self,
        session_proxy: SessionProxy,
        processing_pipeline: ProcessingPipeline = None,
    ) -> None:
        self._session_proxy = session_proxy
        self._settings_service = SettingsService(self._session_proxy)
        self._processing_pipeline = processing_pipeline

    async def configure(
        self, product: Product, processing_pipeline: ProcessingPipeline
    ) -> bool:
        if processing_pipeline is None:
            return False

        self._processing_pipeline = processing_pipeline

        self._processing_pipeline.set_algorithm(product.clustering_algorithm)

        self._processing_pipeline.set_algorithm(product.segmentation_algorithm)

        return self._processing_pipeline is not None

    async def process(self, data: CameraOutput):
        try:
            await self._settings_service.load()

            voxel_size = await self._settings_service.get("voxel_size")

            crop_x_precentage = await self._settings_service.get("crop_precentage_x")

            crop_y_precentage = await self._settings_service.get("crop_precentage_y")

            crop_z_precentage = await self._settings_service.get("crop_precentage_z")

            eps = 3

            iterations = 1000

            cluster_min_points = 10

            cluster_min_points_precentage = await self._settings_service.get(
                "cluster_min_points_precentage"
            )

            row_count = 1

            col_count = 3

            clusters, ground_plane = self._processing_pipeline.process(
                data,
                voxel_size=voxel_size,
                crop_x_precentage=crop_x_precentage,
                crop_y_precentage=crop_y_precentage,
                crop_z_precentage=crop_z_precentage,
                eps=eps,
                iterations=iterations,
                cluster_min_points=cluster_min_points,
                cluster_min_points_precentage=cluster_min_points_precentage,
                row_count=row_count,
                col_count=col_count,
            )

            return clusters, ground_plane[1]
        except Exception as error:
            raise ProcessingError()
