import open3d as o3d
import numpy as np

from app.common.converters.camera_intrinsics import CameraIntrinsicsConverter


class FramesDataConverter:
    @classmethod
    def depth_data_to_cloud(cls, depth_data, intrinsics) -> o3d.geometry.PointCloud:
        summed_cloud = o3d.geometry.PointCloud()

        for data in depth_data:
            depth_array = np.asanyarray(data)

            open3d_depth_image = o3d.geometry.Image(depth_array)

            intrinsic = CameraIntrinsicsConverter.realsense_to_open3d(intrinsics)

            summed_cloud = o3d.geometry.PointCloud.create_from_depth_image(
                open3d_depth_image, intrinsic
            )

        return summed_cloud
