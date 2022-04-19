from typing import Any
from app.models.setting import Setting
from app.enums.setting import MeasurementType
from app.common.converters.millimeters import MillimetersConvertor
from app.common.converters.precentage import PrecentageConvertor


class SettingsValueAdapter:
    @classmethod
    def adapt(cls, setting: Setting) -> Any:
        if setting.measurement == MeasurementType.MILLIMETERS.value:
            return MillimetersConvertor.to_meters(setting.value)
        elif setting.measurement == MeasurementType.PRECENTAGE.value:
            return PrecentageConvertor.to_fraction(setting.value)

        return setting.value
