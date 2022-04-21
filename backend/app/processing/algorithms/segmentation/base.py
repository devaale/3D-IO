import open3d as o3d
from abc import ABC, abstractmethod


class PlaneSegmentationAlgorithm(ABC):
    @abstractmethod
    def execute(
        self,
        cloud: o3d.geometry.PointCloud,
        ransac_n: int,
        iterations: int,
        distance_threshold: float,
    ):
        pass
