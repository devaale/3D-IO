from typing import List, Tuple
import open3d as o3d
from app.services.settings import SettingsService


class PlaneSegmentationRANSAC:
    @classmethod
    async def execute(
        cls, cloud: o3d.geometry.PointCloud, settings: SettingsService
    ) -> List[Tuple[o3d.geometry.PointCloud, List[float]]]:
        ransac_n = 3
        iterations = 1000

        voxel_size = await settings.get("voxel_size")

        distance_threshold = 2 * voxel_size

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
