from typing import List
from typing import TYPE_CHECKING, Optional
from sqlmodel import SQLModel, Relationship, Field
from app.enums.product import ClusteringAlgorithm, PlaneSegmentationAlgorithm
from app.enums.product import ProcessingCommand, ProcessingCommand

if TYPE_CHECKING:
    from app.models.position import PositionModel


class ProductBase(SQLModel):
    product: str = ""
    row_count: int = 1
    col_count: int = 1
    current: bool = False
    created: bool = False
    command: ProcessingCommand = ProcessingCommand.TRAIN
    clustering: ClusteringAlgorithm = ClusteringAlgorithm.DBSCAN
    segmentation: PlaneSegmentationAlgorithm = PlaneSegmentationAlgorithm.RANSAC


class Product(ProductBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    position_models: List["PositionModel"] = Relationship(back_populates="product")


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    id: int


class ProductDelete(ProductBase):
    id: int
