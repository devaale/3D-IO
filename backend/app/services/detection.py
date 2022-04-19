import open3d as o3d
from typing import List
from app.common.helpers import pointcloud
from app.common.converters.position import PositionConverter

from app.services.product import CurrentProductService
from app.services.region import RegionDetectionService
from app.models.position import PositionDetected
from app.services.settings import SettingsService

class DetectionService:
    def __init__(self) -> None:
        self._settings = SettingsService()
        self._product= CurrentProductService()
        self._regions = RegionDetectionService()
        
    async def detect(
        self, clusters: List[o3d.geometry.PointCloud]
    ) -> List[PositionDetected]:
        
        self._settings.load()
        
        detections = []
        
        product = await self._product.get_current()
        
        for i, cluster in enumerate(clusters):
            
            row, col = PositionConverter.convert(i, product.col_count)
            
            position = PositionDetected(row=row, col=col)
            
            position.regions = await self._regions.detect(cluster)
        
        
        cloud = await pointcloud.clusters_to_cloud(clusters)
        
        return cloud, detections
        