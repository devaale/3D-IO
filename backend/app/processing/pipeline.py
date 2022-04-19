import open3d as o3d
from typing import List
from app.common.helpers import pointcloud

from app.services.settings import SettingsService

from app.processing.preprocessing import Preprocessing
from app.processing.clustering.dbscan import ClusteringDBSCAN
from app.processing.segmentation.ransac import PlaneSegmentationRANSAC

class ProcessingPipeline:
    def __init__(self):
        self._settings = SettingsService()

    async def process(self, frames, camera_intrinsics) -> List[o3d.geometry.PointCloud]:
        await self._settings.load()
        
        cloud = await pointcloud.frames_to_cloud(frames, camera_intrinsics)
        
        #preprocessing
        cloud = await Preprocessing.execute(cloud, self._settings)
        
        # plane segmentation
        planes = await PlaneSegmentationRANSAC.execute(cloud, self._settings)

        ground_plane, objects_plane = planes[0], planes[1]
        # clustering
        clusters = await ClusteringDBSCAN.execute(objects_plane[0], self._settings)
        
        clusters = await pointcloud.clusters_sort(clusters, 1, 3)
        
        return clusters
            