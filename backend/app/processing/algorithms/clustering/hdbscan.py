import open3d as o3d
import numpy as np
from typing import List
from app.processing.utils import pointcloud
from app.common.converters.pointcloud import PointCloudConverter
from app.processing.algorithms.clustering.base import ClusteringAlgorithm
import hdbscan


class ClusteringHDBSCAN(ClusteringAlgorithm):
    def __init__(self) -> None:
        pass

    def execute(
        self,
        cloud: o3d.geometry.PointCloud,
        eps: float,
        cluster_min_points: int,
        cluster_min_points_precentage,
    ) -> List[o3d.geometry.PointCloud]:

        clusters_points = self.clusters_find(cloud, cluster_min_points)

        clusters = self.clusters_filter(clusters_points, cluster_min_points_precentage)

        return clusters

    def clusters_find(cloud: o3d.geometry.PointCloud, cluster_min_points: int):
        points = np.asarray(cloud.points)

        model = hdbscan.HDBSCAN(
            algorithm="best",
            alpha=1.0,
            approx_min_span_tree=True,
            gen_min_span_tree=True,
            leaf_size=40,
            metric="euclidean",
            min_cluster_size=10,
            min_samples=None,
            p=None,
        )

        labels = model.fit_predict(points)

        points_clusters = {}

        for point, label in zip(points, labels):
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
