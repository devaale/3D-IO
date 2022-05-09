from enum import auto
from app.enums.base import AutoNameEnum


class CameraType(str, AutoNameEnum):
    REAL_SENSE = auto()


class CameraModel(str, AutoNameEnum):
    D435 = auto()
