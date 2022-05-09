from sqlmodel import SQLModel, Field
from app.enums.camera import CameraType, CameraModel
from typing import Optional


class CameraBase(SQLModel):
    type: str = CameraType.REAL_SENSE
    model: str = CameraModel.D435
    width: int = 848
    height: int = 480
    fps: int = 30
    serial_num: str = "823112061406"


class Camera(CameraBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class CameraCreate(CameraBase):
    pass
