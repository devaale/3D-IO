from app.models.product import Product
from app.processing.factories.clustering import ClusteringAlgorithmFactory
from app.processing.pipelines.pipeline import BasicProcessingPipeline
from app.common.models.camera_data import CameraData
from app.common.converters.frames import FramesDataConverter
from app.processing.factories.segmentation import (
    PlaneSegmentationAlgorithmFactory,
)
from app.services.settings import SettingsService


class ProcessingService:
    def __init__(self) -> None:
        self._processing_pipeline = None

    async def configure(self, settings_service: SettingsService, product: Product):
        clustering_algorithm = ClusteringAlgorithmFactory.create(
            product.clustering_algorithm
        )

        plane_segmentation_algorithm = PlaneSegmentationAlgorithmFactory.create(
            product.segmentation_algorithm
        )

        self._processing_pipeline = BasicProcessingPipeline(
            settings_service, clustering_algorithm, plane_segmentation_algorithm
        )

    async def process(self, camera_data: CameraData):
        cloud = FramesDataConverter.depth_data_to_cloud(
            camera_data.depth_data, camera_data.intrinsics
        )

        clusters = await self._processing_pipeline.process(cloud)

        return clusters
