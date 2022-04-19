from typing import List
from typing import TYPE_CHECKING, Optional
from sqlmodel import Relationship, SQLModel, Field
from app.models.region import RegionDetected


if TYPE_CHECKING:
    from app.models.result import Result
    from app.models.product import Product
    from app.models.region import RegionModel


class PositionModelBase(SQLModel):
    row: int = 0
    col: int = 0
    plane_angle: int = 0


class PositionModel(PositionModelBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    product_id: Optional[int] = Field(default=None, foreign_key="product.id")
    product: Optional["Product"] = Relationship(back_populates="position_models")
    regions: List["RegionModel"] = Relationship(back_populates="position_model")
    results: List["Result"] = Relationship(back_populates="position_model")


class PositionModelCreate(PositionModelBase):
    model_id: int


class PositionModelUpdate(PositionModelBase):
    id: int


class PositionModelDelete(PositionModelBase):
    id: int


class PositionDetected(PositionModelBase):
    regions: List[RegionDetected] = []
