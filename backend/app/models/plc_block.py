from typing import Optional
from sqlmodel import Relationship, SQLModel, Field

from app.models.plc import Plc

class PlcBlockBase(SQLModel):
    name: str = ""
    offset: int = 0
    offset_bit: int = 0
    db_num: int = 0

class PlcBlock(PlcBlockBase, table=True):
    id: int = Field(default=None, primary_key=True)
    plc_id: Optional[int] = Field(default=1, foreign_key="plc.id")
    plc: Optional[Plc] = Relationship(back_populates="blocks")

class PlcBlockCreate(PlcBlockBase):
    pass

class PlcBlockUpdate(PlcBlockBase):
    pass

class PlcBlockDelete(PlcBlockBase):
    pass