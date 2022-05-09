from abc import ABC, abstractclassmethod
from app.common.interfaces.camera.reader import CameraReader


class CameraReaderFactory(ABC):
    @abstractclassmethod
    def create(
        self,
        camera_type: str,
        camera_model: str,
        width: int,
        height: int,
        fps: int,
        serial_num: str,
    ) -> CameraReader:
        pass
