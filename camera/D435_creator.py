from camera import Camera
from camera_D435 import RealSenseD453
from camera_creator import CameraCreator

class RealSenseD435Creator(CameraCreator):
    def create_camera(self) -> Camera:
        return RealSenseD453()