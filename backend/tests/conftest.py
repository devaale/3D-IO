from webbrowser import get
import pytest
import open3d as o3d
from starlette.testclient import TestClient

from backend.main import app
from backend.app.processing.utils import pointcloud
from backend.app.processing.algorithms.plane_segmentation.factory import (
    PlaneSegmentationAlgorithmFactory,
)
from backend.app.processing.algorithms.clustering.factory import (
    ClusteringAlgorithmFactory,
)
from backend.app.processing.algorithms.clustering import dbscan
from backend.app.processing.algorithms.plane_segmentation import ransac
from backend.app.database.session import get_session
import os

current_dir = os.path.dirname(__file__)
cloud_filepath = "cloud_1.pcd"
full_cloud_path = os.path.join(current_dir, cloud_filepath)


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client


@pytest.fixture(scope="module")
def test_session():
    session = get_session()
    yield session


@pytest.fixture
def test_cloud():
    cloud = o3d.io.read_point_cloud(full_cloud_path)
    return cloud


@pytest.fixture
def test_product_cloud():
    cloud = o3d.io.read_point_cloud(full_cloud_path)
    _, product_cloud = ransac.PlaneSegmentationRANSAC().execute(cloud, 3, 1000, 0.005)
    product_cloud_cropped = pointcloud.crop_ptc(product_cloud, [0.9, 1, 1])

    return product_cloud_cropped


@pytest.fixture
def test_dbscan_algorithm():
    algorithm = dbscan.ClusteringDBSCAN()
    return algorithm


@pytest.fixture
def test_ransac_algorithm():
    algorithm = ransac.PlaneSegmentationRANSAC()
    return algorithm


@pytest.fixture
def test_plane_segmentation_factory():
    factory = PlaneSegmentationAlgorithmFactory()
    return factory


@pytest.fixture
def test_clustering_factory():
    factory = ClusteringAlgorithmFactory()
    return factory
