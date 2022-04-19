import open3d as o3d
from app.common.helpers import pointcloud
from app.services.settings import SettingsService


class Preprocessing:
    @classmethod
    async def execute(cls, cloud: o3d.geometry.PointCloud, settings: SettingsService) -> o3d.geometry.PointCloud:
        crop_x = await settings.get('crop_precentage_x')
        crop_y = await settings.get('crop_precentage_y')
        crop_z = await settings.get('crop_precentage_z')
        
        cloud = await pointcloud.crop_ptc(cloud, [crop_x, crop_y, crop_z])
        
        voxel_size = await settings.get('voxel_size')
        
        cloud = await pointcloud.voxel_down_cloud(cloud, voxel_size)
        
        return cloud
    
    