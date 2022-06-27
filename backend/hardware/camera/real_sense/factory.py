from app.common.interfaces.camera.reader import CameraReader
from hardware.camera.real_sense.d435.reader import RealSenseD435Reader


class RealSenseCameraReaderFactory:
    @classmethod
    def create(
        self, camera_model: str, width: int, height: int, fps: int, serial_num: str
    ) -> CameraReader:
        if camera_model == "D435":
            return RealSenseD435Reader(width, height, fps, serial_num)
        else:
            raise Exception(f"Camera type: {camera_model} doesn't exist")
