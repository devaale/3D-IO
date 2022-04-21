import open3d as o3d
from typing import List


class PointCloudConverter:
    @classmethod
    def from_points_to_cloud(cls, points) -> List[o3d.geometry.PointCloud]:
        cloud = o3d.geometry.PointCloud(o3d.utility.Vector3dVector(points))

        return cloud
