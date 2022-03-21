from typing import Optional
from sqlmodel import Relationship, SQLModel, Field

from app.models.plc import Plc
from app.enums.plc_block import (
    PlcBlockCommand,
    PlcBlockMode,
    PlcBlockDataType,
)


class PlcBlockBase(SQLModel):
    desc: str = ""
    offset: int = 0
    offset_bit: int = 0
    db_num: int = 0
    size: int = 1
    mode: PlcBlockMode = PlcBlockMode.READ.value
    data_type: PlcBlockDataType = PlcBlockDataType.BOOL.value
    command: PlcBlockCommand = PlcBlockCommand.CONN_EXIST.value


class PlcBlock(PlcBlockBase, table=True):
    id: int = Field(default=None, primary_key=True)
    plc_id: int = Field(default=1, foreign_key="plc.id")


class PlcBlockCreate(PlcBlockBase):
    pass


class PlcBlockUpdate(PlcBlockBase):
    pass


class PlcBlockDelete(PlcBlockBase):
    pass
