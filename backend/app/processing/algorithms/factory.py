from app.processing.algorithms.store import AlgorithmStore
from app.processing.algorithms.clustering.factory import ClusteringAlgorithmFactory
from app.processing.algorithms.plane_segmentation.factory import (
    PlaneSegmentationAlgorithmFactory,
)


class AbstractAlgorithmFactory:
    @classmethod
    def create(cls, algorithm_type: str):
        algorithm_family = AlgorithmStore.get_family_by_type(algorithm_type)

        if algorithm_family == "CLUSTERING":
            return ClusteringAlgorithmFactory.create(algorithm_type)
        elif algorithm_family == "PLANE_SEGMENTATION":
            return PlaneSegmentationAlgorithmFactory.create(algorithm_type)
