import open3d as o3d
from typing import List
from app.common.helpers import pointcloud
from app.common.converters.position import PositionConverter

from app.services.product import CurrentProductService
from app.models.position import PositionDetected
from app.models.region import RegionDetected
from app.services.settings import SettingsService
from app.enums.region import RegionPosition
from app.processing.feature_extractors.region import RegionExtractor
from app.services.result import ResultService


class DetectionService:
    def __init__(
        self,
        settings_service: SettingsService,
        product_service: CurrentProductService,
        result_service: ResultService,
    ) -> None:
        self._settings = settings_service
        self._product = product_service
        self._region_extractor = RegionExtractor()
        self._result_service = result_service

    async def detect(
        self, clusters: List[o3d.geometry.PointCloud]
    ) -> List[PositionDetected]:

        await self._settings.load()

        product = await self._product.get_current()

        for i, cluster in enumerate(clusters):

            row, col = PositionConverter.to_cell_position(i, product.col_count)

            detected_object = PositionDetected(row=row, col=col, plane_angle=0)

            detected_object.regions = await self.detect_regions(cluster)

            _ = await self._result_service.handle_detection(detected_object)

        cloud = await pointcloud.clusters_to_cloud(clusters)

        return cloud, []

    async def detect_regions(
        self, cloud: o3d.geometry.PointCloud
    ) -> List[RegionDetected]:
        regions = []

        region_size = await self._settings.get("corner_size")

        for position in [x.value for x in RegionPosition]:

            self._region_extractor.execute(cloud, position, region_size)

            depth_mean = self._region_extractor.extract_depth()

            region = RegionDetected(depth_mean=round(depth_mean, 5), position=position)

            regions.append(region)

        return regions
