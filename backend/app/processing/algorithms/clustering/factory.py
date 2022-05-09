from app.processing.algorithms.clustering.dbscan import ClusteringDBSCAN


class ClusteringAlgorithmFactory:
    @classmethod
    def create(cls, clustering_algorithm: str):
        if clustering_algorithm == "DBSCAN":
            return ClusteringDBSCAN()
        else:
            print(f"Clustering algorithm: {clustering_algorithm} doesn't exist")
            raise ValueError()
