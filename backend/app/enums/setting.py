from enum import Enum, auto
from app.enums.base import AutoNameEnum


class SettingType(str, AutoNameEnum):
    PROCESSING_GENERAL = auto()
    PROCESSING_ADVANCED = auto()


class MeasurementType(str, Enum):
    PRECENTAGE = "%"
    MILLIMETERS = "mm"
