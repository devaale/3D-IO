import open3d as o3d
import numpy as np
from typing import List
from app.common.helpers import pointcloud
from app.common.converters.pointcloud import PointCloudConverter
from app.processing.algorithms.clustering.base import ClusteringAlgorithm


class ClusteringDBSCAN(ClusteringAlgorithm):
    def __init__(self) -> None:
        pass

    def execute(
        self,
        cloud: o3d.geometry.PointCloud,
        eps: float,
        cluster_min_points: int,
        cluster_min_points_precentage,
    ) -> List[o3d.geometry.PointCloud]:

        clusters_points = self.clusters_find(cloud, cluster_min_points, eps)

        clusters = self.clusters_filter(clusters_points, cluster_min_points_precentage)

        return clusters

    def clusters_find(
        self, cloud: o3d.geometry.PointCloud, cluster_min_points: int, eps: int
    ):
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
        self, clusters_points, cluster_min_pts_precentage
    ) -> List[o3d.geometry.PointCloud]:
        clusters = []

        max_pts_cluster = pointcloud.clouds_find_max_points(clusters_points)

        min_pts_cluster = int(max_pts_cluster * cluster_min_pts_precentage)

        clusters_points = pointcloud.clusters_filter(clusters_points, min_pts_cluster)

        for cluster_points in clusters_points:
            cluster_cloud = PointCloudConverter.from_points_to_cloud(cluster_points)
            clusters.append(cluster_cloud)

        return clusters
