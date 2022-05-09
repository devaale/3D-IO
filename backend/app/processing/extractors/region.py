import open3d as o3d
import numpy as np
from typing import List
from app.processing.utils import pointcloud, math
from app.processing.algorithms.factory import AbstractAlgorithmFactory


class RegionExtractor:
    def __init__(self) -> None:
        self._cloud = o3d.geometry.PointCloud()
        self._region_points = []

    def extract(
        self, cloud: o3d.geometry.PointCloud, region_position: str, region_size: float
    ):
        self._cloud = cloud

        self._region_points = []

        oriented_bounding_box = pointcloud.get_oriented_bounding_box(cloud)

        min_x, min_y, max_x, max_y = pointcloud.get_bounds_x_y(oriented_bounding_box)

        region_min_x, region_max_x = pointcloud.get_bounds_x(
            region_position, region_size, min_x, max_x
        )

        region_min_y, region_max_y = pointcloud.get_bounds_y(
            region_position, region_size, min_y, max_y
        )

        self._region_points = pointcloud.get_bounded_points_x_y(
            np.asarray(cloud.points),
            region_min_x,
            region_max_x,
            region_min_y,
            region_max_y,
        )

    def get_depth_mean(self) -> float:
        depth_mean = math.calculate_mean_by_axis(data=self._region_points, axis=2)

        return depth_mean

    def get_plane_angle(self):
        plane_segmentation_algorithm = AbstractAlgorithmFactory.create("RANSAC")

        plane, _ = plane_segmentation_algorithm.execute(
            self._cloud, 3, 1000, 0.005, planes_to_extract=1
        )

        return plane[0][1]

    def get_points(self) -> List[List[float]]:
        return self._region_points
