from typing import TYPE_CHECKING, Optional
from sqlmodel import Relationship, SQLModel, Field

from app.models.plc import Plc
from app.enums.plc_block import (
    PlcBlockCommand,
    PlcBlockMode,
    PlcBlockDataType,
    PlcBlockByteSize,
)

if TYPE_CHECKING:
    from app.models.plc import Plc


class PlcBlockBase(SQLModel):
    desc: Optional[str] = ""
    offset: int = 0
    offset_bit: int = 0
    db_num: int = 0
    size: int = PlcBlockByteSize.BOOL
    mode: PlcBlockMode = PlcBlockMode.READ
    data_type: PlcBlockDataType = PlcBlockDataType.BOOL
    command: PlcBlockCommand = PlcBlockCommand.CONNECTED


class PlcBlock(PlcBlockBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    plc_id: Optional[int] = Field(default=1, foreign_key="plc.id")
    plc: Optional["Plc"] = Relationship(back_populates="blocks")


class PlcBlockCreate(PlcBlockBase):
    pass


class PlcBlockUpdate(PlcBlockBase):
    id: int


class PlcBlockDelete(PlcBlockBase):
    id: int
