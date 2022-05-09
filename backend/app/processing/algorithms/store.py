class AlgorithmStore:
    STORE = {"DBSCAN": "CLUSTERING", "RANSAC": "PLANE_SEGMENTATION"}

    @classmethod
    def get_family_by_type(cls, type: str) -> str:
        return cls.STORE[type]
