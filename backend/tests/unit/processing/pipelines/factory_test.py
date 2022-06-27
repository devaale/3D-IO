from backend.app.processing.factory import (
    PointCloudProcessingPipelineFactory,
)
from backend.app.processing.pipelines.default import (
    DefaultProcessingPipeline,
)


def test_create_default_pipeline():
    ransac = PointCloudProcessingPipelineFactory().create("TEST")
    assert type(ransac).__name__ == "DefaultProcessingPipeline"
