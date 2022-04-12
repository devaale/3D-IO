import os
from threading import Lock
from app.utils import pointcloud, json
from app.services.settings_proxy import SettingsProxy

import open3d as o3d


class ProcessingService:
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
    PROC_SETTINGS_FILE = "C:\\Users\\evald\\Documents\\Coding\\Projects\\University\\3D-IO\\backend\\app\\services\\settings.json"
    
    def __init__(self):
        self._lock = Lock()

        self.detect = False
        self._models = None
        self._curr_product = None

        self._settings = SettingsProxy()

    # @property
    # def product(self) -> Product:
    #     with self._lock:
    #         return self._curr_product

    # # TODO: Change ORM to SQL model and fetch data as product.models
    # # TODO: Set settings service - use JSONFileService to read data
    # # TODO: Or add web settings and access settings via self._curr_product.settings
    # @product.setter
    # def product(self, product: Product):
    #     with self._lock:
    #         self._curr_product = product
    #         self._models = functions.get_references(self._curr_product.id)
    #         self._settings.load(JSONFileService().read(self.FILE_PATH))
    #         self._detect = self._curr_product.has_reference

    #         print(f"Updated product to: {self._curr_product.model}")
    #         print(f"Model count: {len(self._models)}")
    #         print(f"Settings value: {self._settings.get('depth_from')}")
    #         print(f"Detect: {self._detect}")

    def process(self, frames, camera_intrinsics):
        #TODO: Get settings from database
        
        json_dict = json.read_json_dict(self.PROC_SETTINGS_FILE)
        
        self._settings.load(json_dict)
        
        cloud = o3d.geometry.PointCloud()
        
        # pre-processing
        cloud = pointcloud.frames_to_cloud(frames, camera_intrinsics)
        
        cloud = pointcloud.crop_ptc(cloud, [0.8, 1, 1])
                
        cloud = pointcloud.remove_points_bot(cloud, float(self._settings.get('depth_to')))
            
        cloud = pointcloud.remove_points_top(cloud, float(self._settings.get('depth_from')))
        
        cloud = pointcloud.voxel_down_cloud(cloud, float(self._settings.get('voxel_down')))
        
        # clustering 
        eps = 2 * float(self._settings.get('voxel_down'))
                        
        clusters_points = pointcloud.clusters_find(cloud, 10, eps)
        
        clusters = pointcloud.clusters_get(clusters_points, self._settings.get('precentage_of_average_points_cluster'))
        
        cloud = pointcloud.clusters_to_cloud(clusters)
        
        o3d.visualization.draw_geometries([cloud])
            
            
            