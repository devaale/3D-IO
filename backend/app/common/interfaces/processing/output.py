from typing import List
from abc import ABC, abstractmethod


class ProcessingOutput(ABC):
    @abstractmethod
    def get_cloud_points(self, processing_step: str) -> List[List[float]]:
        pass

    @abstractmethod
    def get_cluster_points(self, row: int = 1, col: int = 1) -> List[List[float]]:
        pass
