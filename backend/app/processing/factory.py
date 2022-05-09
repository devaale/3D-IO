from app.processing.pipelines.default import DefaultProcessingPipeline
from app.common.interfaces.processing.pipeline_factory import ProcessingPipelineFactory


class PointCloudProcessingPipelineFactory(ProcessingPipelineFactory):
    @classmethod
    def create(self, product_type: str):
        if product_type == "TEST":
            return DefaultProcessingPipeline()
        else:
            raise ValueError()
