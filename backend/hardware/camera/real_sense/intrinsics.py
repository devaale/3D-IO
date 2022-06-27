
import pyrealsense2 as rs

from app.common.interfaces.camera.intrinsics import CameraIntrinsics


class RealSenseIntrinsics(CameraIntrinsics):
    def __init__(self, intrinsics: rs.intrinsics) -> None:
        self._intrinsics = intrinsics
    
    def get_width(self) -> int:
        return self._intrinsics.width

    def get_height(self) -> int:
        return self._intrinsics.height

    def get_fx(self) -> float:
        return self._intrinsics.fx

    def get_fy(self) -> float:
        return self._intrinsics.fy

    def get_ppx(self) -> float:
        return self._intrinsics.ppx

    def get_ppy(self) -> float:
        return self._intrinsics.ppy
    