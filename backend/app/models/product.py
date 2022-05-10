from typing import List
from typing import TYPE_CHECKING, Optional
from sqlmodel import SQLModel, Relationship, Field
from app.enums.product import ClusteringAlgorithm, PlaneSegmentationAlgorithm
from app.enums.product import ProcessingCommand, ProcessingCommand
from app.enums.product import ProductModel

if TYPE_CHECKING:
    from app.models.result import Result
    from app.models.position import PositionModel


class ProductBase(SQLModel):
    model: str = ProductModel.TEST
    row_count: int = 1
    col_count: int = 1
    current: bool = False
    created: bool = False
    command: ProcessingCommand = ProcessingCommand.TRAIN
    clustering_algorithm: ClusteringAlgorithm = ClusteringAlgorithm.DBSCAN
    segmentation_algorithm: PlaneSegmentationAlgorithm = (
        PlaneSegmentationAlgorithm.RANSAC
    )


class Product(ProductBase, table=True):
    __table_args__ = {"extend_existing": True}
    id: Optional[int] = Field(default=None, primary_key=True)
    position_models: List["PositionModel"] = Relationship(back_populates="product")
    position_results: List["Result"] = Relationship(back_populates="product")


class ProductCreate(ProductBase):
    pass


class ProductRead(ProductBase):
    pass


class ProductUpdate(ProductBase):
    id: Optional[int]


class ProductDelete(ProductBase):
    id: Optional[int]
