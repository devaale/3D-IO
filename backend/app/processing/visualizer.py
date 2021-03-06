import open3d as o3d
import cv2
from typing import List


class Visualizer:
    def __init__(self):
        self._source = o3d.geometry.PointCloud

        self._processed_clouds = {}

        self._cloud_to_show_type = ""

        self._grid_lines = o3d.geometry.Geometry

        self._boxes_lines = o3d.geometry.Geometry

        self._visualiser = o3d.visualization.Visualizer()

        self._created = False

        self._cloud_added = False

    def start(self):
        if self._created:
            return
        self._created = True
        self._visualiser.create_window()

    def visualize_cloud(self, source: o3d.geometry.PointCloud):
        if source is None or not self._created:
            return

        if self._cloud_added:
            self._source.points = source.points
            self._source.colors = source.colors

            self._visualiser.update_geometry(self._source)
            self._visualiser.poll_events()
            self._visualiser.update_renderer()

        self._source = source
        self._visualiser.add_geometry(self._source)
        self._cloud_added = True

    def add_boxes_lines(self, source: o3d.geometry.Geometry):
        self._boxes_lines = source

        self._visualiser.add_geometry(self._boxes_lines, reset_bounding_box=False)

    def update_boxes_lines(self, source: o3d.geometry.Geometry):
        self._visualiser.remove_geometry(self._boxes_lines, reset_bounding_box=False)

        self._boxes_lines = source

        self._visualiser.add_geometry(self._boxes_lines, reset_bounding_box=False)

    def add_grid(self, source: o3d.geometry.Geometry):
        self._grid_lines = source

        self._visualiser.add_geometry(self._grid_lines, reset_bounding_box=False)

    def update_grid(self, grid_lines: o3d.geometry.Geometry):
        self._visualiser.remove_geometry(self._grid_lines, reset_bounding_box=False)

        self._grid_lines = grid_lines

        self._visualiser.add_geometry(self._grid_lines, reset_bounding_box=False)

    def is_closed(self) -> bool:
        return not self._visualiser.poll_events()

    def stop(self):
        if not self._created:
            return
        self._created = False
        self._visualiser.destroy_window()

    def __del__(self):
        self.stop()

    @staticmethod
    def visualize_color_frame(color_data: List[float]):
        cv2.namedWindow("RGB Camera", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("RGB Camera", color_data)
        cv2.waitKey(1)
