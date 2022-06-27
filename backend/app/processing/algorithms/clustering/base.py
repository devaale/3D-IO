import open3d as o3d
from abc import ABC, abstractmethod


class ClusteringAlgorithm(ABC):
    @abstractmethod
    def execute(
        self,
        cloud: o3d.geometry.PointCloud,
        eps: float,
        cluster_min_points: int,
        cluster_min_points_precentage,
    ):
        pass
