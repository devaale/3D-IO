from enum import Enum

class SettingType(int, Enum):
    PROCESSING_GENERAL = 10
    PROCESSING_ADVANCED = 20

class MeasurementType(str, Enum):
    PRECENTAGE = "%"
    MILLIMETERS = "mm"
