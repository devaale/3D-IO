from typing import List
from typing import TYPE_CHECKING, Optional
from sqlmodel import Relationship, SQLModel, Field
from app.models.region import RegionDetected
from app.models.region import RegionModelCreate


if TYPE_CHECKING:
    from app.models.product import Product
    from app.models.region import RegionModel


class PositionModelBase(SQLModel):
    row: int = 0
    col: int = 0
    plane_angle: int = 0


class PositionModel(PositionModelBase, table=True):
    __table_args__ = {"extend_existing": True}
    id: Optional[int] = Field(default=None, primary_key=True)
    product_id: Optional[int] = Field(default=None, foreign_key="product.id")
    product: Optional["Product"] = Relationship(back_populates="position_models")
    regions: List["RegionModel"] = Relationship(back_populates="position_model")


class PositionModelCreate(PositionModelBase):
    product_id: Optional[int]
    regions: Optional[List[RegionModelCreate]]


class PositionModelUpdate(PositionModelBase):
    id: Optional[int]


class PositionModelDelete(PositionModelBase):
    id: Optional[int]


class PositionDetected(PositionModelBase):
    product_id: Optional[int]
    regions: Optional[List[RegionDetected]] = []
