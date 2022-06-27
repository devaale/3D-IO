from sqlmodel import SQLModel, Field
from app.enums.setting import MeasurementType


class SettingBase(SQLModel):
    key: str = ""
    description: str = ""
    value: float = 5
    min_value: float = 0
    max_value: float = 10
    step: float = 1
    measurement: MeasurementType = MeasurementType.MILLIMETERS


class Setting(SettingBase, table=True):
    __table_args__ = {"extend_existing": True}
    id: int = Field(default=None, primary_key=True)


class SettingUpdate(SettingBase):
    pass


class SettingCreate(SettingBase):
    pass


class SettingDelete(SettingBase):
    id: int
