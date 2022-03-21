from typing import List
from sqlmodel import Relationship, SQLModel, Field


class PlcBase(SQLModel):
    ip: str = "0.0.0.0"
    rack: int = 0
    slot: int = 0


class Plc(PlcBase, table=True):
    id: int = Field(default=None, primary_key=True)


class PlcCreate(PlcBase):
    pass


class PlcUpdate(PlcBase):
    pass


class PlcDelete(PlcBase):
    pass
