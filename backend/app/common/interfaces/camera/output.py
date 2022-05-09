from abc import ABC, abstractmethod
from app.common.interfaces.camera.intrinsics import CameraIntrinsics
from typing import List


class CameraOutput(ABC):
    @abstractmethod
    def get_depth_data(self) -> List[List[float]]:
        pass

    @abstractmethod
    def get_color_data(self) -> List[List[float]]:
        pass

    @abstractmethod
    def get_camera_intrinsics(self) -> CameraIntrinsics:
        pass
