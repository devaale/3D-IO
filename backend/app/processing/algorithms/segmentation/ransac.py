from typing import List, Tuple
import open3d as o3d
from app.processing.algorithms.segmentation.base import PlaneSegmentationAlgorithm


class PlaneSegmentationRANSAC(PlaneSegmentationAlgorithm):
    @classmethod
    async def execute(
        cls,
        cloud: o3d.geometry.PointCloud,
        ransac_n: int,
        iterations: int,
        distance_threshold: float,
    ) -> List[Tuple[o3d.geometry.PointCloud, List[float]]]:

        planes = []

        cloud_outlier = cloud

        for _ in range(2):
            plane_model, inliers = cloud_outlier.segment_plane(
                distance_threshold, ransac_n, iterations
            )

            plane_cloud = cloud_outlier.select_by_index(inliers)

            planes.append((plane_cloud, plane_model))

            cloud_outlier = cloud_outlier.select_by_index(inliers, True)

        return planes
