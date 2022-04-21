import open3d as o3d
from typing import List
from app.common.helpers import pointcloud

from app.services.settings import SettingsService

from app.processing.preprocessing import Preprocessing
from app.processing.algorithms.segmentation.base import PlaneSegmentationAlgorithm
from app.processing.algorithms.clustering.base import ClusteringAlgorithm
from app.processing.pipelines.base import ProcessingPipeline

class BasicProcessingPipeline(ProcessingPipeline):
    def __init__(self, settings_service: SettingsService, clustering_algorithm: ClusteringAlgorithm, plane_segmentation_algorithm: PlaneSegmentationAlgorithm):
        self._settings = settings_service
        self._clustering_algorithm = clustering_algorithm
        self._plane_segmentation_algorithm = plane_segmentation_algorithm

    async def process(self, cloud: o3d.geometry.PointCloud) -> List[o3d.geometry.PointCloud]:
        await self._settings.load()
        
        voxel_size = await self._settings.get("voxel_size")
        
        cluster_min_points_precentage = await self._settings.get("cluster_min_size_precentage")
        #preprocessing
        cloud = await Preprocessing.execute(cloud, self._settings)
        
        distance_threshold = voxel_size * 2
        # plane segmentation
        planes = await self._plane_segmentation_algorithm.execute(cloud, 3, 1000, distance_threshold)

        ground_plane, objects_plane = planes[0], planes[1]
        # clustering
        clusters = self._clustering_algorithm.execute(objects_plane[0], voxel_size * 2, 10, cluster_min_points_precentage)
        
        clusters = await pointcloud.clusters_sort(clusters, 1, 3)
        
        return clusters
        
            