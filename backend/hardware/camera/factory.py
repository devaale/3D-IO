from app.common.interfaces.camera.reader import CameraReader
from app.common.interfaces.camera.reader_factory import CameraReaderFactory
from hardware.camera.real_sense.factory import RealSenseCameraReaderFactory


class AbstractCameraReaderFactory(CameraReaderFactory):
    @classmethod
    def create(
        self,
        type: str,
        model: str,
        width: int,
        height: int,
        fps: int,
        serial_num: str,
    ) -> CameraReader:
        if type == "REAL_SENSE":
            return RealSenseCameraReaderFactory.create(
                model, width, height, fps, serial_num
            )
        else:
            raise Exception(f"Camera type: {type} doesn't exist")
