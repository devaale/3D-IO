from abc import ABC, abstractmethod


class SessionProxy(ABC):
    @abstractmethod
    def get(self):
        pass
