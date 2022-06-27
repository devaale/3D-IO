import open3d as o3d
from app.processing.utils import pointcloud


class Preprocessing:
    @classmethod
    def execute(cls, cloud: o3d.geometry.PointCloud, voxel_size: float, crop_x_precentage: float, crop_y_precentage: float, crop_z_precentage: float) -> o3d.geometry.PointCloud:        
        cloud = pointcloud.crop_ptc(cloud, [crop_x_precentage, crop_y_precentage, crop_z_precentage])
        
        cloud = pointcloud.voxel_down_cloud(cloud, voxel_size)
        
        return cloud
    
    