import open3d as o3d
import numpy as np
from typing import List
from app.processing import utils
from app.common.helpers import math
from app.models.region import RegionDetected
from app.enums.region import RegionPosition
from app.services.settings import SettingsService
from app.common.adapters.region_bound import RegionBoundAdapter


class RegionDetectionService:
    def __init__(self) -> None:
        self._settings = SettingsService()

    async def detect(self, cloud: o3d.geometry.PointCloud) -> List[RegionDetected]:
        regions = []

        await self._settings.load()

        region_size = await self._settings.get("corner_size")

        oriented_bounding_box = utils.get_oriented_bounding_box(cloud)

        min_x, min_y, max_x, max_y = utils.get_bounds_x_y(oriented_bounding_box)

        for position in [x.value for x in RegionPosition]:
            region_min_x, region_max_x = RegionBoundAdapter.get_bounds_x(
                position, region_size, min_x, max_x
            )

            region_min_y, region_max_y = RegionBoundAdapter.get_bounds_y(
                position, region_size, min_y, max_y
            )

            points = utils.get_bounded_points_x_y(
                np.asarray(cloud.points),
                region_min_x,
                region_max_x,
                region_min_y,
                region_max_y,
            )

            depth_mean = math.calculate_mean_by_axis(data=points, axis=2)

            region = RegionDetected(depth_mean=round(depth_mean, 5), position=position)

            regions.append(region)

        return regions
