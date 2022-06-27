from abc import ABC, abstractmethod


class CameraReader(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass
