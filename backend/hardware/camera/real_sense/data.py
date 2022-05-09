import pyrealsense2 as rs
from typing import List
import numpy as np
from app.common.interfaces.camera.output import CameraOutput
from hardware.camera.real_sense.intrinsics import RealSenseIntrinsics


class RealSenseData(CameraOutput):
    def __init__(
        self,
        depth_frames: List[rs.frame],
        color_frames: List[rs.frame],
        intrinsics: rs.intrinsics,
    ) -> None:
        self._depth_frames = depth_frames
        self._color_frames = color_frames
        self._intrinsics = intrinsics

    def get_depth_data(self) -> List[List[float]]:
        depth_data = []

        print("I'm here -> realsense data")
        for depth_frame in self._depth_frames:
            depth_data.append(np.asanyarray(depth_frame.get_data()))

        return depth_data

    def get_color_data(self) -> List[List[float]]:
        color_data = []

        for color_frame in self._color_frames:
            color_data.append(np.asanyarray(color_frame.get_data()))

        return color_data

    def get_camera_intrinsics(self) -> RealSenseIntrinsics:
        return RealSenseIntrinsics(self._intrinsics)
