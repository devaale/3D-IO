from abc import ABC, abstractmethod
from threading import Thread


class Service(Thread, ABC):
    def __init__(self):
        Thread.__init__(self)
        self.setDaemon(True)
        self.running = True

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def stop(self):
        pass
