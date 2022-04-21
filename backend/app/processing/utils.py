from typing import List
import numpy as np
import open3d as o3d
from app.enums.region import RegionPosition
from app.processing import math


def get_oriented_bounding_box(
    cloud: o3d.geometry.PointCloud,
) -> o3d.geometry.OrientedBoundingBox:

    axis_aligned_bounding_box = cloud.get_axis_aligned_bounding_box()

    base_extent = axis_aligned_bounding_box.get_extent()

    extent = np.array(
        [
            [base_extent[0]],
            [base_extent[1]],
            [base_extent[2]],
        ]
    )

    base_center = axis_aligned_bounding_box.get_center()

    center = np.array(
        [
            base_center[0],
            base_center[1],
            base_center[2],
        ]
    )

    return o3d.geometry.OrientedBoundingBox(center, np.identity(3), extent)


def get_bounds_x_y(bounding_box: o3d.geometry.OrientedBoundingBox) -> List[float]:
    min_x_y = bounding_box.get_min_bound()
    max_x_y = bounding_box.get_max_bound()
    bounds_x_y = [min_x_y[0], min_x_y[1], max_x_y[0], max_x_y[1]]
    return bounds_x_y


def get_bounded_points_x_y(
    points: List[List[float]], min_x: float, max_x: float, min_y: float, max_y: float
):
    points_bounded = points[
        (points[:, 0] >= min_x)
        & (points[:, 0] <= max_x)
        & (points[:, 1] >= min_y)
        & (points[:, 1] <= max_y)
    ]
    return points_bounded


def get_bounds_x(
    position: str,
    size: float,
    cloud_min_x: float,
    cloud_max_x: float,
) -> List[float]:

    if (
        position == RegionPosition.LEFT_BOT.value
        or position == RegionPosition.LEFT_TOP.value
    ):
        min_x = cloud_min_x
        max_x = math.fraction(cloud_min_x, cloud_max_x, size)
    elif (
        position == RegionPosition.RIGHT_BOT.value
        or position == RegionPosition.RIGHT_TOP.value
    ):
        min_x = math.fraction(cloud_max_x, cloud_min_x, size)
        max_x = cloud_max_x
    else:
        min_x = cloud_min_x
        max_x = cloud_max_x

    return min_x, max_x


def get_bounds_y(position: str, size: float, cloud_min_y: float, cloud_max_y: float):

    if (
        position == RegionPosition.LEFT_BOT.value
        or position == RegionPosition.RIGHT_BOT.value
    ):
        min_y = cloud_min_y
        max_y = math.fraction(cloud_min_y, cloud_max_y, size)
    elif (
        position == RegionPosition.LEFT_TOP.value
        or position == RegionPosition.RIGHT_TOP.value
    ):
        min_y = math.fraction(cloud_max_y, cloud_min_y, size)
        max_y = cloud_max_y
    else:
        min_y = cloud_min_y
        max_y = cloud_max_y

    return min_y, max_y
