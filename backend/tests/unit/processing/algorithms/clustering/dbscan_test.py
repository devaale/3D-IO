from backend.app.processing.algorithms.clustering import dbscan

def test_dbscan_execute(test_product_cloud, test_dbscan_algorithm):
    result = test_dbscan_algorithm.execute(test_product_cloud, 0.005, 10, 0.8)
    result_count = len(result)
    assert result_count == 3

def test_dbscan_clusters_find(test_product_cloud, test_dbscan_algorithm):
    result = test_dbscan_algorithm.clusters_find(test_product_cloud, 10, 0.005)
    result_count = len(result.items())
    assert result_count == 9

def test_dbscan_clusters_filter(test_product_cloud, test_dbscan_algorithm):
    clusters = test_dbscan_algorithm.clusters_find(test_product_cloud, 10, 0.005)
    result = test_dbscan_algorithm.clusters_filter(clusters, 0.8)
    result_count = len(result)
    assert result_count == 3
    