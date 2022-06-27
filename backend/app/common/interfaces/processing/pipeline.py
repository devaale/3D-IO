from abc import ABC, abstractmethod
from app.common.interfaces.camera.output import CameraOutput


class ProcessingPipeline(ABC):
    @abstractmethod
    def process(
        self,
        data: CameraOutput,
        voxel_size: float = 0.0025,
        crop_x_precentage: float = 1,
        crop_y_precentage: float = 1,
        crop_z_precentage: float = 1,
        eps: int = 3,
        iterations: int = 1000,
        cluster_min_points: int = 10,
        cluster_min_points_precentage: float = 0.5,
        row_count: int = 1,
        col_count: int = 1,
    ):
        pass

    @abstractmethod
    def set_algorithm(self, algorithm_type: str):
        pass
