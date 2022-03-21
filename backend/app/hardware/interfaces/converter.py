from abc import ABC, abstractmethod


class Converter:
    @abstractmethod
    def convert_to(self):
        pass

    @abstractmethod
    def convert_from(self, value):
        pass
