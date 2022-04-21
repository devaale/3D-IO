from abc import ABC
from abc import ABC, abstractmethod


class SessionProxy(ABC):
    @abstractmethod
    def get(self):
        pass
