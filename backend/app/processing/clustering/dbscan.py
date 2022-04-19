import open3d as o3d
from typing import List
from app.common.helpers import pointcloud
from app.services.settings import SettingsService


class ClusteringDBSCAN:
    @classmethod
    async def execute(
        cls, cloud: o3d.geometry.PointCloud, settings: SettingsService
    ) -> List[o3d.geometry.PointCloud]:
        voxel_size = await settings.get("voxel_size")

        eps = 2 * voxel_size

        clusters_points = await pointcloud.clusters_find(cloud, 10, eps)

        cluster_min_size_precentage = await settings.get("cluster_min_size_precentage")

        clusters = await pointcloud.clusters_get(
            clusters_points, cluster_min_size_precentage
        )

        return clusters
