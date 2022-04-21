import open3d as o3d
import numpy as np
from app.processing import utils, math


class RegionExtractor:
    def __init__(self) -> None:
        self._region_points = []

    def execute(
        self, cloud: o3d.geometry.PointCloud, region_position: str, region_size: float
    ):

        self._region_points = []

        oriented_bounding_box = utils.get_oriented_bounding_box(cloud)

        min_x, min_y, max_x, max_y = utils.get_bounds_x_y(oriented_bounding_box)

        region_min_x, region_max_x = utils.get_bounds_x(
            region_position, region_size, min_x, max_x
        )

        region_min_y, region_max_y = utils.get_bounds_y(
            region_position, region_size, min_y, max_y
        )

        self._region_points = utils.get_bounded_points_x_y(
            np.asarray(cloud.points),
            region_min_x,
            region_max_x,
            region_min_y,
            region_max_y,
        )

    def extract_depth(self) -> float:
        depth_mean = math.calculate_mean_by_axis(data=self._region_points, axis=2)

        return depth_mean

    def extract_plane_angle(self):
        pass
