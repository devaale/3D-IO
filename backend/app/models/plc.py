from typing import TYPE_CHECKING, List, Optional
from sqlmodel import Relationship, SQLModel, Field

if TYPE_CHECKING:
    from app.models.plc_block import PlcBlock


class PlcBase(SQLModel):
    ip: Optional[str] = Field(default=None)
    rack: Optional[int] = Field(default=None)
    slot: Optional[int] = Field(default=None)


class Plc(PlcBase, table=True):
    __table_args__ = {"extend_existing": True}
    id: Optional[int] = Field(default=None, primary_key=True)
    blocks: List["PlcBlock"] = Relationship(back_populates="plc")


class PlcCreate(PlcBase):
    pass


class PlcRead(PlcBase):
    id: int


class PlcUpdate(PlcBase):
    id: int


class PlcDelete(PlcBase):
    id: int
