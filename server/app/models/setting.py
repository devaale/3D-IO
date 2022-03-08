from sqlmodel import SQLModel, Field

from ..enums.setting import MeasurementType, SettingType

class SettingBase(SQLModel):
    label: str
    value: float
    min_value: float
    max_value: float
    type: SettingType = SettingType.PROCESSING_GENERAL.value
    measurement: MeasurementType = MeasurementType.PRECENTAGE.value


class Setting(SettingBase, table=True):
    id: int = Field(default=None, primary_key=True)


class SettingUpdate(SettingBase):
    pass

class SettingCreate(SettingBase):
    pass