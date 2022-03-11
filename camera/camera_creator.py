from camera import Camera
from abc import ABC, abstractmethod

class CameraCreator(ABC):
    @abstractmethod
    def create_camera(self) -> Camera:
        pass