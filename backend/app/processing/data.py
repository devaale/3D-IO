import open3d as o3d

from app.processing.extractors.region import RegionExtractor
from app.common.interfaces.processing.output import ProcessingOutput


class ProcessedDataAdapter(ProcessingOutput):
    def __init__(self) -> None:
        self._row_count = 1
        self._col_count = 3

        self._processed_clouds = {}
        self._position_depth_data = []

        self._region_extractor = RegionExtractor()

    def add_cloud(self, cloud: o3d.geometry.PointCloud, cloud_type: str):
        self._processed_clouds[cloud_type] = cloud

    def get_(
        self,
        row: int,
        col: int,
        region_position: str,
        region_size: float,
    ) -> float:
        cluster = self.__get_cluster(row, col)

        self._region_extractor.extract(cluster, region_position, region_size)

        return self._region_extractor.get_depth_mean()

    def __get_cluster(self, row: int, col: int):
        try:
            index = col + row * self._row_count
            return self._processed_clouds["CLUSTERS"][index]
        except Exception as error:
            raise ValueError(f"Can't find cluster in row: {row}, col: {col}") from error
