from backend.app.processing.algorithms.plane_segmentation.ransac import (
    PlaneSegmentationRANSAC,
)
from backend.app.processing.algorithms.plane_segmentation.factory import (
    PlaneSegmentationAlgorithmFactory,
)


def test_create_ransac_algorithm(test_plane_segmentation_factory):
    ransac = PlaneSegmentationAlgorithmFactory().create("RANSAC")
    assert type(ransac).__name__ == "PlaneSegmentationRANSAC"
