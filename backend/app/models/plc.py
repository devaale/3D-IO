from typing import List
from sqlmodel import Relationship, SQLModel, Field

class PlcBase(SQLModel):
    ip: str = 'default'
    rack: int = 0
    slot: int = 0


class Plc(PlcBase, table=True):
    id: int = Field(default=None, primary_key=True)
    blocks: List["PlcBlock"] = Relationship(back_populates="plc")

class PlcCreate(PlcBase):
    pass

class PlcUpdate(PlcBase):
    pass

class PlcDelete(PlcBase):
    pass