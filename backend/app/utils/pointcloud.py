import open3d as o3d
import numpy as np
import pyrealsense2 as rs
from typing import List

from typing import List
import open3d as o3d


def voxel_down_cloud(
    cloud: o3d.geometry.PointCloud, voxel_size: float
) -> o3d.geometry.PointCloud:

    cloud_down_sampled = cloud.voxel_down_sample(voxel_size)

    return cloud_down_sampled


def clusters_find(cloud: o3d.geometry.PointCloud, cluster_min_points: int, eps: int):
    labels = np.array(
        cloud.cluster_dbscan(
            min_points=cluster_min_points, eps=eps, print_progress=True
        )
    )

    points_clusters = {}

    for point, label in zip(cloud.points, labels):
        if label != -1:
            points_clusters[label] = points_clusters.get(label, [])
            points_clusters[label].append(point)

    return points_clusters


def clusters_filter(
    points_clusters, min_pts_cluster: int
) -> List[o3d.geometry.PointCloud]:
    clusters_clouds = []

    for _, points_cluster in points_clusters.items():
        if len(points_cluster) > min_pts_cluster:
            cluster_points = o3d.geometry.PointCloud(
                o3d.utility.Vector3dVector(points_cluster)
            )
            clusters_clouds.append(cluster_points)

    return clusters_clouds


def clouds_get_max_pts(clusters_points) -> int:
    try:
        result = len(max(clusters_points.values(), key=lambda x: len(x)))
    except ValueError:
        return 0

    return result


def crop_ptc(
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


def clusters_to_cloud(
    clusters: List[o3d.geometry.PointCloud],
) -> o3d.geometry.PointCloud:
    cloud = o3d.geometry.PointCloud()

    for cluster in clusters:
        cloud += cluster

    return cloud


def clusters_get(
    clusters_points, cluster_min_pts_precentage
) -> List[o3d.geometry.PointCloud]:
    clusters = []

    max_pts_cluster = clouds_get_max_pts(clusters_points)

    min_pts_cluster = int(max_pts_cluster * cluster_min_pts_precentage)

    clusters = clusters_filter(clusters_points, min_pts_cluster)

    return clusters


def frames_to_cloud(
    frames: List[rs.depth_frame], camera_intrinsics
) -> o3d.geometry.PointCloud:
    cloud = o3d.geometry.PointCloud()

    for frame in frames:
        cloud += create_cloud_from_frame(frame, camera_intrinsics)

    return cloud


def create_cloud_from_frame(
    depth_frame: rs.depth_frame, camera_intrinsic: rs.intrinsics
) -> o3d.geometry.PointCloud:
    depth_array = np.asanyarray(depth_frame.get_data())

    open3d_depth_image = o3d.geometry.Image(depth_array)

    intrinsic = __pinhole_camera_intrinsic(camera_intrinsic)

    cloud = o3d.geometry.PointCloud.create_from_depth_image(
        open3d_depth_image, intrinsic
    )

    return cloud


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


def divide_to_planes(
    cloud: o3d.geometry.PointCloud,
    threshold_distance: float = 0.001,
    ransac_n: int = 3,
    iterations: int = 1000,
    planes_to_extract_count: int = 2,
):
    planes = []

    cloud_temp = cloud

    for _ in range(planes_to_extract_count):
        model, inliers = __export_plane_inliers(
            cloud_temp, threshold_distance, ransac_n, iterations
        )

        plane = cloud_temp.select_by_index(inliers)

        planes.append((plane, model))

        cloud_temp = cloud_temp.select_by_index(inliers, True)

        if len(cloud_temp.points) < 3:
            raise Exception("plane division error")

    if len(planes) < 2:
        raise Exception("only one plane extracted")

    return planes


def filter_planes(planes):
    planes.sort(key=__sort_planes_by_single_axis, reverse=True)

    return planes[0][0], planes[1][0], planes[1][1]


def __pinhole_camera_intrinsic(
    camera_intrinsic: rs.intrinsics,
) -> o3d.camera.PinholeCameraIntrinsic:
    return o3d.camera.PinholeCameraIntrinsic(
        camera_intrinsic.width,
        camera_intrinsic.height,
        camera_intrinsic.fx,
        camera_intrinsic.fy,
        camera_intrinsic.ppx,
        camera_intrinsic.ppy,
    )


def __sort_planes_by_single_axis(cloud_with_model, axis: int = 2):
    depth = cloud_with_model[0].get_center()[axis]
    return depth


def __sort_clusters_by_single_axis(
    clusters_clouds: List[o3d.geometry.PointCloud], axis: int = 0, reverse: bool = True
) -> List[o3d.geometry.PointCloud]:
    sorted_clusters = sorted(
        clusters_clouds, key=lambda x: x.get_center()[axis], reverse=reverse
    )

    return sorted_clusters


def __export_plane_inliers(
    cloud: o3d.geometry.PointCloud, threshold: float, ransac: int, iterations: int
):
    plane_model, inliers = cloud.segment_plane(threshold, ransac, iterations)
    return plane_model, inliers
