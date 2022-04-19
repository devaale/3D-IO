from typing import List
import numpy as np
import open3d as o3d


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

def get_bounded_points_x_y(points: List[List[float]], min_x: float, max_x: float, min_y: float, max_y: float):
    points_bounded = points[
        (points[:, 0] >= min_x)
        & (points[:, 0] <= max_x)
        & (points[:, 1] >= min_y)
        & (points[:, 1] <= max_y)
    ]
    return points_bounded
    
        
    