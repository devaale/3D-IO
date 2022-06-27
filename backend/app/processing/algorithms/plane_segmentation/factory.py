from app.processing.algorithms.plane_segmentation.ransac import PlaneSegmentationRANSAC


class PlaneSegmentationAlgorithmFactory:
    @classmethod
    def create(cls, segmentation_algorithm: str):
        if segmentation_algorithm == "RANSAC":
            return PlaneSegmentationRANSAC()
        else:
            return PlaneSegmentationRANSAC()
