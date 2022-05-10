from typing import Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Relationship, Field
from app.enums.region import RegionPosition


if TYPE_CHECKING:
    from app.models.position import PositionModel


class RegionModelBase(SQLModel):
    position: Optional[RegionPosition] = RegionPosition.LEFT_BOT
    depth_mean: Optional[float]


class RegionModel(RegionModelBase, table=True):
    __table_args__ = {"extend_existing": True}
    id: Optional[int] = Field(default=None, primary_key=True)
    position_model_id: Optional[int] = Field(
        default=None, foreign_key="positionmodel.id"
    )
    position_model: Optional["PositionModel"] = Relationship(back_populates="regions")


class RegionModelUpdate(RegionModelBase):
    pass


class RegionModelCreate(RegionModelBase):
    pass


class RegionModelDelete(RegionModelBase):
    id: int


class RegionDetected(RegionModelBase):
    position_model_id: Optional[int]
