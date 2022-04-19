from enum import auto
from app.enums.base import AutoNameEnum


class MeasurementType(str, AutoNameEnum):
    PRECENTAGE = auto()
    MILLIMETERS = auto()
