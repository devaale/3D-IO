from backend.app.processing.algorithms.clustering.dbscan import (
    ClusteringDBSCAN,
)
from backend.app.processing.algorithms.clustering.factory import (
    ClusteringAlgorithmFactory,
)


def test_create_dbscan_algorithm():
    dbscan = ClusteringAlgorithmFactory().create("DBSCAN")
    assert type(dbscan).__name__ == "ClusteringDBSCAN"
