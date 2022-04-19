from enum import auto
from app.enums.base import AutoNameEnum


class ClusteringAlgorithm(str, AutoNameEnum):
    DBSCAN = auto()
    KMEANS = auto()
    OPTICS = auto()


class PlaneSegmentationAlgorithm(str, AutoNameEnum):
    RANSAC = auto()
    MLESAC = auto()
    PROSAC = auto()


class ProcessingCommand(str, AutoNameEnum):
    TRAIN = auto()
    DETECT = auto()
