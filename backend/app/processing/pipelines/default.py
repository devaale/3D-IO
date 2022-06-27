import open3d as o3d
from typing import List

from app.processing.utils import pointcloud
from app.processing.utils.preprocessing import Preprocessing

from app.processing.algorithms.clustering.base import ClusteringAlgorithm
from app.processing.algorithms.plane_segmentation.base import PlaneSegmentationAlgorithm
from app.processing.algorithms.factory import AbstractAlgorithmFactory
from app.processing.algorithms.store import AlgorithmStore

from app.common.interfaces.processing.pipeline import ProcessingPipeline
from app.common.interfaces.camera.output import CameraOutput
from app.common.interfaces.processing.input import ProcessingInput

class DefaultProcessingPipeline(ProcessingPipeline):
    def __init__(self, clustering_algorithm: ClusteringAlgorithm = None, plane_segmentation_algorithm: PlaneSegmentationAlgorithm = None):
        self._clustering_algorithm = clustering_algorithm
        self._plane_segmentation_algorithm = plane_segmentation_algorithm

    def set_algorithm(self, algorithm_type: str):
        algorithm_family = AlgorithmStore.get_family_by_type(algorithm_type)
        
        if algorithm_family == "CLUSTERING":
            self._clustering_algorithm = AbstractAlgorithmFactory.create(
                algorithm_type
            )
        elif algorithm_family == "PLANE_SEGMENTATION":
            self._plane_segmentation_algorithm = AbstractAlgorithmFactory.create(
                algorithm_type
            )
        else:
            raise ValueError()
        
        
    def process(self, input_data: ProcessingInput, voxel_size: float = 0.0025, crop_x_precentage: float = 1, crop_y_precentage: float = 1, crop_z_precentage: float = 1, eps: int = 3, iterations: int = 1000, cluster_min_points: int = 10, cluster_min_points_precentage: float = 0.5, row_count: int = 1, col_count: int = 1) -> List[o3d.geometry.PointCloud]:
        print("[PIPELINE] Started.")
        
        cloud = pointcloud.depth_data_to_cloud(input_data.get_depth_data(), input_data.get_camera_intrinsics())
        
        cloud = Preprocessing.execute(cloud, voxel_size, crop_x_precentage, crop_y_precentage, crop_z_precentage)
        
        distance_threshold = voxel_size * 2

        ground_plane, objects_cloud = self._plane_segmentation_algorithm.execute(cloud, eps, iterations, distance_threshold)
        
        clusters = self._clustering_algorithm.execute(objects_cloud, voxel_size * 2, cluster_min_points, cluster_min_points_precentage)
        
        clusters = pointcloud.clusters_sort(clusters, row_count, col_count)
        
        return clusters, ground_plane[0]
        
            