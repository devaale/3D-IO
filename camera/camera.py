from abc import ABC, abstractmethod

from enums import CameraType

class Camera(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def __del__(self):
        pass