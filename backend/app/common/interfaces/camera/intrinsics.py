from abc import ABC, abstractmethod


class CameraIntrinsics(ABC):
    @abstractmethod
    def get_width(self) -> int:
        pass

    @abstractmethod
    def get_height(self) -> int:
        pass

    @abstractmethod
    def get_fx(self) -> float:
        pass

    @abstractmethod
    def get_fy(self) -> float:
        pass

    @abstractmethod
    def get_ppx(self) -> float:
        pass

    @abstractmethod
    def get_ppy(self) -> float:
        pass
