from typing import List
from app.common.interfaces.processing.input import ProcessingInput
from app.common.interfaces.camera.output import CameraOutput


class CameraOutputAdapter:
    def __init__(self, camera_output: CameraOutput):
        self._camera_output = camera_output
        self._processing_input = None

    def to_processing_input(self, processing_input: ProcessingInput) -> ProcessingInput:
        self._processing_input = processing_input

        self.set_depth_data()

        self.set_camera_intrinsics()

    def set_camera_intrinsics(self):
        camera_intrinsics = self._camera_output.get_camera_intrinsics()
        self._processing_input.set_camera_intrinsics(
            camera_intrinsics.get_width(),
            camera_intrinsics.get_height(),
            camera_intrinsics.get_fx(),
            camera_intrinsics.get_fy(),
            camera_intrinsics.get_ppx(),
            camera_intrinsics.get_ppy(),
        )

    def set_depth_data(self):
        depth_data = self._camera_output.get_depth_data()

        self._processing_input.set_depth_data(depth_data)
