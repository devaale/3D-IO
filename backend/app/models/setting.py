from sqlmodel import SQLModel, Field

from app.enums.setting import MeasurementType, SettingType


class SettingBase(SQLModel):
    label: str = "default"
    value: float = 5
    min_value: float = 0
    max_value: float = 10
    step: float = 1
    type: SettingType = SettingType.PROCESSING_GENERAL.value
    measurement: MeasurementType = MeasurementType.MILLIMETERS.value


class Setting(SettingBase, table=True):
    id: int = Field(default=None, primary_key=True)


class SettingUpdate(SettingBase):
    pass


class SettingCreate(SettingBase):
    pass


class SettingDelete(SettingBase):
    id: int
