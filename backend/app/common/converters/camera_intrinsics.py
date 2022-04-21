import open3d as o3d
import pyrealsense2 as rs


class CameraIntrinsicsConverter:
    @classmethod
    def realsense_to_open3d(
        cls,
        intrinsics: rs.intrinsics,
    ) -> o3d.camera.PinholeCameraIntrinsic:
        return o3d.camera.PinholeCameraIntrinsic(
            intrinsics.width,
            intrinsics.height,
            intrinsics.fx,
            intrinsics.fy,
            intrinsics.ppx,
            intrinsics.ppy,
        )
