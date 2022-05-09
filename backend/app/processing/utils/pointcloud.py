from typing import List
import pyrealsense2 as rs
from app.enums.region import RegionPosition
import numpy as np
import open3d as o3d
import math as m
from app.processing.utils import math
from app.common.interfaces.camera.intrinsics import CameraIntrinsics


def depth_data_to_cloud(
    depth_data: List[List[float]], intrinsics: CameraIntrinsics
) -> o3d.geometry.PointCloud:
    summed_cloud = o3d.geometry.PointCloud()

    for data in depth_data:
        depth_array = np.asanyarray(data)

        open3d_depth_image = o3d.geometry.Image(depth_array)

        intrinsic = o3d.camera.PinholeCameraIntrinsic(
            intrinsics.get_width(),
            intrinsics.get_height(),
            intrinsics.get_fx(),
            intrinsics.get_fy(),
            intrinsics.get_ppx(),
            intrinsics.get_ppy(),
        )

        print(
            intrinsics.get_width(),
            intrinsics.get_height(),
            intrinsics.get_fx(),
            intrinsics.get_fy(),
            intrinsics.get_ppx(),
            intrinsics.get_ppy(),
        )

        summed_cloud = o3d.geometry.PointCloud.create_from_depth_image(
            open3d_depth_image, intrinsic
        )

    return summed_cloud


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


COLORS = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
    [0.4, 0.9, 0],
    [0.4, 0.3, 0],
    [0.7, 0.4, 0.2],
    [0.1, 0.7, 0.7],
    [0.1, 0.1, 0.6],
    [0.8, 0.4, 0.2],
    [0.5, 0.9, 0.4],
]


def normals_vectors_angle(first: List[float], second: List[float]) -> float:
    return m.fabs(sum(first[0:3] * second[0:3])) / (
        m.sqrt(sum(np.square(first[0:3]))) * m.sqrt(sum(np.square(second[0:3])))
    )


def angle_to_degrees(angle: float) -> float:
    return round(np.degrees(angle * np.pi / 2), 4)


def voxel_down_cloud(
    cloud: o3d.geometry.PointCloud, voxel_size: float
) -> o3d.geometry.PointCloud:

    cloud_down_sampled = cloud.voxel_down_sample(voxel_size)

    return cloud_down_sampled


def clusters_filter(
    points_clusters, min_points_threshold: int
) -> List[o3d.geometry.PointCloud]:
    filtered = []

    for _, points_cluster in points_clusters.items():
        if len(points_cluster) > min_points_threshold:
            filtered.append(points_cluster)

    return filtered


def clouds_find_max_points(clusters_points) -> int:
    try:
        result = len(max(clusters_points.values(), key=lambda x: len(x)))
    except ValueError:
        return 0

    return result


def crop_ptc(
    cloud: o3d.geometry.PointCloud, crop_percentile: List[float]
) -> o3d.geometry.PointCloud:
    axis_aligned_bounding_box = cloud.get_axis_aligned_bounding_box()

    base_extent = axis_aligned_bounding_box.get_extent()
    base_center = axis_aligned_bounding_box.get_center()

    extent = np.array(
        [
            [base_extent[0] * crop_percentile[0]],
            [base_extent[1] * crop_percentile[1]],
            [base_extent[2] * crop_percentile[2]],
        ]
    )

    bounding_box = o3d.geometry.OrientedBoundingBox(base_center, np.identity(3), extent)

    return cloud.crop(bounding_box)


def clusters_to_cloud(
    clusters: List[o3d.geometry.PointCloud],
) -> o3d.geometry.PointCloud:
    cloud = o3d.geometry.PointCloud()

    for cluster in clusters:
        cloud += cluster

    return cloud


def sort_clusters_by_single_axis(
    clusters_clouds: List[o3d.geometry.PointCloud], axis: int = 0, reverse: bool = True
) -> List[o3d.geometry.PointCloud]:
    sorted_clusters = sorted(
        clusters_clouds, key=lambda x: x.get_center()[axis], reverse=reverse
    )

    return sorted_clusters


def clusters_sort(
    clusters: List[o3d.geometry.PointCloud], row_count: int, col_count: int
) -> List[o3d.geometry.PointCloud]:
    clusters_sorted = []

    clusters_sorted_y = sort_clusters_by_single_axis(clusters, 1, reverse=True)

    for i in range(row_count):
        clusters_row = clusters_sorted_y[i * col_count : (i + 1) * col_count]

        clusters_sorted_x = sort_clusters_by_single_axis(clusters_row, 0, reverse=False)

        clusters_sorted += clusters_sorted_x

    return clusters_sorted


def colorize_clouds(clouds: List[o3d.geometry.PointCloud]):
    index = -1
    count = 0

    for cloud in clouds:
        if count % 3 == 0:
            index += 1
        cloud.paint_uniform_color(COLORS[count])
        count += 1


def rotate_cloud_correct_position(cloud: o3d.geometry.PointCloud):
    rotation_matrix = cloud.get_rotation_matrix_from_xyz((np.pi, 0, 0))

    center = cloud.get_center()

    cloud.rotate(rotation_matrix, center)


def create_image_from_frame(depth_frame: rs.depth_frame):
    depth_array = np.asanyarray(depth_frame.get_data())

    open3d_depth_image = o3d.geometry.Image(depth_array)

    return open3d_depth_image


def remove_points_bot(
    cloud: o3d.geometry.PointCloud, bound: float
) -> o3d.geometry.PointCloud:
    cloud_points = np.asarray(cloud.points)

    valid_points = cloud_points[(cloud_points[:, 2] < bound - 0.0005)]

    cloud.points = o3d.utility.Vector3dVector(valid_points)

    return cloud


def remove_points_top(
    cloud: o3d.geometry.PointCloud, bound: float
) -> o3d.geometry.PointCloud:
    cloud_points = np.asarray(cloud.points)

    valid_points = cloud_points[(cloud_points[:, 2] > bound)]

    cloud.points = o3d.utility.Vector3dVector(valid_points)

    return cloud


def filter_planes(planes):
    planes.sort(key=sort_planes_by_single_axis, reverse=True)

    return planes[0][0], planes[1][0], planes[1][1]


def sort_planes_by_single_axis(cloud_with_model, axis: int = 2):
    depth = cloud_with_model[0].get_center()[axis]
    return depth
