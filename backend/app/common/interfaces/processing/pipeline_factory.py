from abc import ABC, abstractclassmethod
from app.common.interfaces.processing.pipeline import ProcessingPipeline


class ProcessingPipelineFactory(ABC):
    @abstractclassmethod
    def create(self, product_model: str) -> ProcessingPipeline:
        pass
