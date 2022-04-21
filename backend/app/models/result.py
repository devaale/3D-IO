from typing import TYPE_CHECKING, Optional
from sqlmodel import Relationship, SQLModel, Field


if TYPE_CHECKING:
    from app.models.product import Product


class ResultBase(SQLModel):
    valid: bool = False
    depth_error: float = 0


class Result(ResultBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    product_id: Optional[int] = Field(default=None, foreign_key="product.id")
    product: Optional["Product"] = Relationship(back_populates="position_results")


class ResultCreate(ResultBase):
    position_model_id: int = 1


class ResultUpdate(ResultBase):
    id: int


class ResultDelete(ResultBase):
    id: int
