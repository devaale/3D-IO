from app.hardware.camera.real_sense.reader import RealSenseCameraReader


class CameraReaderFactory:
    @classmethod
    def create(
        self, camera_type: str, width: int, height: int, fps: int, serial_num: str
    ):
        if camera_type == "REAL_SENSE":
            return RealSenseCameraReader(width, height, fps, serial_num)
        else:
            raise Exception(f"Camera type: {camera_type} doesn't exist")
