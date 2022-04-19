from typing import Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Relationship, Field
from app.enums.region import RegionPosition


if TYPE_CHECKING:
    from app.models.position import PositionModel


class RegionModelBase(SQLModel):
    position: RegionPosition = RegionPosition.LEFT_BOT
    depth_mean: float


class RegionModel(RegionModelBase, table=True):
    id: int = Field(default=None, primary_key=True)
    position_model_id: Optional[int] = Field(
        default=None, foreign_key="positionmodel.id"
    )
    position_model: Optional["PositionModel"] = Relationship(back_populates="regions")


class RegionModelUpdate(RegionModelBase):
    pass


class RegionModelCreate(RegionModelBase):
    position_model_id: int


class RegionModelDelete(RegionModelBase):
    id: int


class RegionDetected(RegionModelBase):
    pass
