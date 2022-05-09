from unittest import result
import open3d as o3d
import numpy as np
import math as m

from sklearn import cluster
from backend.app.processing.utils import math, pointcloud


def test_get_oriented_bounding_box(test_cloud):
    bounds = [int(x) for x in test_cloud.get_max_bound()]
    oriented_box = pointcloud.get_oriented_bounding_box(test_cloud)
    oriented_box_bound = [int(x) for x in oriented_box.get_max_bound()]
    assert bounds == oriented_box_bound


def test_get_bounds_x_y(test_cloud):
    oriented_box = pointcloud.get_oriented_bounding_box(test_cloud)
    bounds_x_y = pointcloud.get_bounds_x_y(oriented_box)
    assert bounds_x_y == bounds_x_y


def test_get_bounded_points_x_y():
    points = np.asarray([[0, 0, 0], [1, 1, 1], [2, 2, 2]])
    bounded_x_y = list(pointcloud.get_bounded_points_x_y(points, 3, 3, 3, 3))
    assert bounded_x_y == []


def test_get_bounds_x_left_bot():
    min_x, max_x = pointcloud.get_bounds_x("LEFT_BOT", 0.5, 0, 1)
    assert min_x == 0
    assert max_x == 0.5


def test_get_bounds_x_left_top():
    min_x, max_x = pointcloud.get_bounds_x("LEFT_TOP", 0.5, 0, 1)
    assert min_x == 0
    assert max_x == 0.5


def test_get_bounds_x_right_bot():
    min_x, max_x = pointcloud.get_bounds_x("RIGHT_BOT", 0.5, 0, 1)
    assert min_x == 0.5
    assert max_x == 1


def test_get_bounds_x_right_top():
    min_x, max_x = pointcloud.get_bounds_x("RIGHT_TOP", 0.5, 0, 1)
    assert min_x == 0.5
    assert max_x == 1


def test_get_bounds_y_left_bot():
    min_x, max_x = pointcloud.get_bounds_y("LEFT_BOT", 0.5, 0, 1)
    assert min_x == 0
    assert max_x == 0.5


def test_get_bounds_y_left_top():
    min_x, max_x = pointcloud.get_bounds_y("LEFT_TOP", 0.5, 0, 1)
    assert min_x == 0.5
    assert max_x == 1


def test_get_bounds_y_right_bot():
    min_x, max_x = pointcloud.get_bounds_y("RIGHT_BOT", 0.5, 0, 1)
    assert min_x == 0
    assert max_x == 0.5


def test_get_bounds_y_right_top():
    min_x, max_x = pointcloud.get_bounds_y("RIGHT_TOP", 0.5, 0, 1)
    assert min_x == 0.5
    assert max_x == 1


def test_normals_vector_to_angle():
    result = int(
        pointcloud.normals_vectors_angle(np.asarray([1, 2, 3]), np.asarray([4, 5, 6]))
    )
    assert result == 0


def test_angle_to_degrees():
    result = pointcloud.angle_to_degrees(0)
    assert result == 0


def test_voxel_down_cloud(test_cloud):
    result = pointcloud.voxel_down_cloud(test_cloud, 0.005)
    result_point_cloud = len(np.asanyarray(result.points))
    assert result_point_cloud == 3389


def tests_clusters_filter_zero(test_cloud):
    cluster_points = o3d.utility.Vector3dVector(np.asarray(test_cloud.points))
    result = pointcloud.clusters_filter({0: [cluster_points]}, 100)
    assert len(result) == 0


def tests_clusters_filter_one(test_cloud):
    cluster_points = list(np.asarray(test_cloud.points))
    result = pointcloud.clusters_filter({0: [cluster_points]}, 0)
    assert len(result) == 1


def test_clouds_find_max_points(test_cloud):
    result = pointcloud.clouds_find_max_points({0: [test_cloud]})
    assert result == 1


def test_crop_ptc(test_cloud):
    result = pointcloud.crop_ptc(test_cloud, [1.1, 1.1, 1.1])
    cloud_points = len(test_cloud.points)
    result_points = len(result.points)
    assert result_points == cloud_points


def test_clusters_to_clouds(test_cloud):
    clusters = [test_cloud, test_cloud, test_cloud]
    result = pointcloud.clusters_to_cloud(clusters)
    cloud_points = len(test_cloud.points)
    result_points = len(result.points)
    assert result_points == cloud_points * 3


def test_sort_clusters_by_single_axis(test_cloud):
    clusters = [test_cloud, test_cloud, test_cloud]
    result = pointcloud.sort_clusters_by_single_axis(clusters, 0, False)
    assert result == clusters


def test_clusters_sort(test_cloud):
    clusters = [test_cloud, test_cloud, test_cloud]
    result = pointcloud.clusters_sort(clusters, 1, 3)
    assert result == clusters


def test_rotate_cloud_correct_position(test_cloud):
    cloud_one = o3d.geometry.PointCloud(test_cloud)
    cloud_one.points = o3d.utility.Vector3dVector(np.random.rand(100, 3))
    cloud_two = o3d.geometry.PointCloud(test_cloud)
    cloud_two.points = o3d.utility.Vector3dVector(np.random.rand(100, 3))
    result = pointcloud.rotate_cloud_correct_position(cloud_one)
    assert cloud_one != cloud_two


def test_remove_points_bot(test_cloud):
    bound = test_cloud.get_max_bound()[2] + 10
    result = pointcloud.remove_points_bot(test_cloud, bound)
    assert result == test_cloud


def test_remove_points_top(test_cloud):
    bound = test_cloud.get_max_bound()[2] + 10
    result = pointcloud.remove_points_top(test_cloud, bound)
    assert result == test_cloud


def test_filter_planes(test_cloud):
    plane_one, plane_two, plane_model = pointcloud.filter_planes(
        [[test_cloud, [1, 2, 3]], [test_cloud, [1, 2, 3]]]
    )
    assert plane_one == test_cloud
    assert plane_two == test_cloud
    assert plane_model == [1, 2, 3]
