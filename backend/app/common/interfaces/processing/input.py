from typing import List
from abc import ABC, abstractmethod


class ProcessingInput(ABC):
    @abstractmethod
    def set_depth_data(self, depth_data: List[List[float]]):
        pass

    @abstractmethod
    def set_camera_intrinsics(
        self, width: int, height: int, px: float, py: float, ppx: float, ppy: float
    ):
        pass
