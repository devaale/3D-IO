from abc import ABC, abstractmethod


class CameraReader(ABC):
    @abstractmethod
    async def read(self, frame_count: int):
        pass

    @abstractmethod
    async def connect(self):
        pass

    @abstractmethod
    async def disconnect(self):
        pass
