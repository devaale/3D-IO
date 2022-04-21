import open3d as o3d
import numpy as np
import pyrealsense2 as rs
from typing import List
import math
from typing import List
import open3d as o3d

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


async def normals_vectors_angle(first: List[float], second: List[float]) -> float:
    return math.fabs(sum(first[0:3] * second[0:3])) / (
        math.sqrt(sum(np.square(first[0:3]))) * math.sqrt(sum(np.square(second[0:3])))
    )


async def angle_to_degrees(angle: float) -> float:
    return round(np.degrees(angle * np.pi / 2), 4)


async def voxel_down_cloud(
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


async def crop_ptc(
    cloud: o3d.geometry.PointCloud, crop_percentile: List[int]
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


async def clusters_to_cloud(
    clusters: List[o3d.geometry.PointCloud],
) -> o3d.geometry.PointCloud:
    cloud = o3d.geometry.PointCloud()

    for cluster in clusters:
        cloud += cluster

    return cloud


async def sort_clusters_by_single_axis(
    clusters_clouds: List[o3d.geometry.PointCloud], axis: int = 0, reverse: bool = True
) -> List[o3d.geometry.PointCloud]:
    sorted_clusters = sorted(
        clusters_clouds, key=lambda x: x.get_center()[axis], reverse=reverse
    )

    return sorted_clusters


async def clusters_sort(
    clusters: List[o3d.geometry.PointCloud], row_count: int, col_count: int
) -> List[o3d.geometry.PointCloud]:
    clusters_sorted = []

    clusters_sorted_y = await sort_clusters_by_single_axis(clusters, 1, reverse=True)

    for i in range(row_count):
        clusters_row = clusters_sorted_y[i * col_count : (i + 1) * col_count]

        clusters_sorted_x = await sort_clusters_by_single_axis(
            clusters_row, 0, reverse=False
        )

        clusters_sorted += clusters_sorted_x

    return clusters_sorted


async def colorize_clouds(clouds: List[o3d.geometry.PointCloud]):
    index = -1
    count = 0

    for cloud in clouds:
        if count % 3 == 0:
            index += 1
        cloud.paint_uniform_color(COLORS[count])
        count += 1


async def rotate_cloud_correct_position(cloud: o3d.geometry.PointCloud):
    rotation_matrix = cloud.get_rotation_matrix_from_xyz((np.pi, 0, 0))

    center = cloud.get_center()

    cloud.rotate(rotation_matrix, center)


async def create_image_from_frame(depth_frame: rs.depth_frame):
    depth_array = np.asanyarray(depth_frame.get_data())

    open3d_depth_image = o3d.geometry.Image(depth_array)

    return open3d_depth_image


async def remove_points_bot(
    cloud: o3d.geometry.PointCloud, bound: float
) -> o3d.geometry.PointCloud:
    cloud_points = np.asarray(cloud.points)

    valid_points = cloud_points[(cloud_points[:, 2] < bound - 0.0005)]

    cloud.points = o3d.utility.Vector3dVector(valid_points)

    return cloud


async def remove_points_top(
    cloud: o3d.geometry.PointCloud, bound: float
) -> o3d.geometry.PointCloud:
    cloud_points = np.asarray(cloud.points)

    valid_points = cloud_points[(cloud_points[:, 2] > bound)]

    cloud.points = o3d.utility.Vector3dVector(valid_points)

    return cloud


async def filter_planes(planes):
    planes.sort(key=__sort_planes_by_single_axis, reverse=True)

    return planes[0][0], planes[1][0], planes[1][1]


async def __sort_planes_by_single_axis(cloud_with_model, axis: int = 2):
    depth = cloud_with_model[0].get_center()[axis]
    return depth
