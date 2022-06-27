from backend.app.common.interfaces.camera.output import CameraOutput
from backend.app.processing.pipelines.default import DefaultProcessingPipeline


# def test_default_processing_pipeline_execute(
#     test_cloud, test_ransac_algorithm, test_dbscan_algorithm
# ):
#     processing_pipeline = DefaultProcessingPipeline(
#         test_ransac_algorithm, test_dbscan_algorithm
#     )

#     result = processing_pipeline.process(test_cloud)

#     assert len(result) == 3
