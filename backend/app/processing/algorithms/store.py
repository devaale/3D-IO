class AlgorithmStore:
    STORE = {
        "DBSCAN": "CLUSTERING",
        "RANSAC": "PLANE_SEGMENTATION",
        "HDBSCAN": "CLUSTERING",
    }

    @classmethod
    def get_family_by_type(cls, type: str) -> str:
        return cls.STORE[type]
