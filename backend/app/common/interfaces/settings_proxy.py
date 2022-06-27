from abc import ABC, abstractmethod


class SettingsProxy(ABC):
    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def get(self, key: str):
        pass
