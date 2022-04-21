from abc import ABC, abstractmethod


class ProcessingPipeline(ABC):
    @abstractmethod
    async def process(self, cloud):
        pass
