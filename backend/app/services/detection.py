import open3d as o3d
from typing import List
from app.processing.utils import pointcloud
from app.common.converters.position import PositionConverter
import math
import numpy as np
from app.services.product import CurrentProductService
from app.models.position import PositionDetected
from app.models.region import RegionDetected
from app.services.settings import SettingsService
from app.enums.region import RegionPosition
from app.services.result import ResultService
from app.processing.extractors.region import RegionExtractor
from app.common.errors.detection import DetectionError


class DetectionService:
    def __init__(
        self,
        settings_service: SettingsService,
        product_service: CurrentProductService,
        result_service: ResultService,
    ) -> None:
        self._settings = settings_service
        self._product = product_service
        self._result_service = result_service
        self._region_extractor = RegionExtractor()
        self._angles = []

    async def detect(
        self, clusters: List[o3d.geometry.PointCloud], ground_plane
    ) -> List[PositionDetected]:

        try:
            await self._settings.load()

            product = await self._product.get_current()

            region_size = await self._settings.get("region_size")

            for i, cluster in enumerate(clusters):

                row, col = PositionConverter.to_cell_position(i, product.col_count)

                detected_object = PositionDetected(row=row, col=col, plane_angle=0)

                detected_object.regions = self.detect_regions(
                    cluster, region_size, ground_plane
                )

                _ = await self._result_service.handle_detection(
                    detected_object, product.id
                )

            cloud = pointcloud.clusters_to_cloud(clusters)

            return cloud
        except Exception as error:
            raise DetectionError("Failed to detect")

    def detect_regions(
        self, cloud: o3d.geometry.PointCloud, region_size: float, ground_plane
    ) -> List[RegionDetected]:

        regions = []

        for position in [x.value for x in RegionPosition]:
            self._region_extractor.extract(cloud, position, region_size)

            depth_mean = self._region_extractor.get_depth_mean()

            plane = self._region_extractor.get_plane_angle()

            angle = self.normals_vectors_angle(plane, ground_plane)

            degrees = self.angle_to_degrees(angle)

            self._angles.append(degrees)

            region = RegionDetected(depth_mean=round(depth_mean, 5), position=position)

            regions.append(region)

        return regions

    def normals_vectors_angle(self, first, second) -> float:
        return math.fabs(sum(first[0:3] * second[0:3])) / (
            math.sqrt(sum(np.square(first[0:3])))
            * math.sqrt(sum(np.square(second[0:3])))
        )

    def angle_to_degrees(self, angle: float) -> float:
        return round(np.degrees(angle * np.pi / 2), 4)
