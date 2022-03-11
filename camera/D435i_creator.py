from camera import Camera
from camera_D435i import RealSenseD453i
from camera_creator import CameraCreator

class RealSenseD435iCreator(CameraCreator):
    def create_camera(self) -> Camera:
        return RealSenseD453i()