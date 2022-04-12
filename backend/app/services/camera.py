import time
from threading import Event

from typing import *

from app.errors.camera import CameraError
from app.hardware.camera.reader import CameraReader
from app.services.processing import ProcessingService

# from desktop_app.services.visualization.depth import Visualizer3D
# from desktop_app.services.visualization.rgb import VisualizerRGB
# from desktop_app.services.visualization.result import VisualizerResult


class CameraService:
    SAMPLE_COUNT = 5

    def __init__(self):
        self._results = dict()
        self._results_db = list()

        # self._settings = SettingsProxy()

        self._trigger = Event()

        self._proc_service = ProcessingService()
        self._camera_reader = CameraReader(848, 480, 30, "823112061406")
        # self._visualizer3D = Visualizer3D()
        # self._visualizerRGB = VisualizerRGB()
        # self._visualizer_result = VisualizerResult()

    def set_manual_reference(self):
        self._proc_service.detect = False
        self._trigger.set()

    def set_manual_detect(self):
        self._proc_service.detect = True
        self._trigger.set()

    def connect(self):
        try:
            return self._camera_reader.connect()
        except CameraError as error:
            print(error)

    def disconnect(self):
        try:
            return not self._camera_reader.disconnect()
        except CameraError as error:
            print(error)

    def connected(self) -> bool:
        try:
            return self._camera_reader.connected()
        except CameraError as error:
            print(error)

    def run(self):
        self.connect()

        try:
            while True:
                if self._trigger.is_set():

                    # TODO: Get sample count from database
                    depth_frames = []
                    color_frames = []

                    try:
                        depth_frames, color_frames = self._camera_reader.read(
                            self.SAMPLE_COUNT
                        )
                    except CameraError as error:
                        print(error)
                        continue

                    self._proc_service.process(
                        depth_frames, self._camera_reader.intrinsics()
                    )

                    # self.__save_results()
                    # self._visualizer_result.update(self._results)
                    # self.__clear_results()
                    self._trigger.clear()

                time.sleep(0.001)
        finally:
            self.disconnect()

    # def _visualize(self):
    #     depth_frames, color_frames = self._camera_reader.read(1)
    #     results_cloud = self.__run_detection(depth_frames)
    #     self._visualizer3D.render(utils.sum_points_colors_to_cloud(results_cloud))
    #     self._visualizerRGB.render(color_frames[0])

    # @timing
    # def __camera_post_processing(
    #     self, depth_frames: List[rs.depth_frame]
    # ) -> List[rs.depth_frame]:
    #     frames = []

    #     for depth_frame in depth_frames:
    #         frame = Camera.apply_threshold_filter(
    #             depth_frame,
    #             self._settings.get("depth_from"),
    #             self._settings.get("depth_to"),
    #         )
    #         frame = Camera.apply_temporal_filter(frame)
    #         frames.append(frame)

    #     return frames

    # def __run_detection(self, depth_frames: List[rs.depth_frame]):
    #     logger.info(
    #         "[Camera Service] Running clustering processing strategy. Detecting."
    #     )
    #     frames = self.__camera_post_processing(depth_frames)
    #     results_cloud = clustering_detection.detect(
    #         frames[0],
    #         frames,
    #         0,
    #         self._camera_reader.intrinsics(),
    #         self._settings,
    #         self._references,
    #         self.__selected_product,
    #         self._results,
    #         self._results_db,
    #         self.DETECTION_RESULT_FOLDER,
    #     )

    #     return results_cloud

    # def __run_reference_creation(self, depth_frames: List[rs.depth_frame]):
    #     logger.info(
    #         "[Camera Service] Running clustering processing strategy. Creating Reference."
    #     )
    #     frames = self.__camera_post_processing(depth_frames)

    #     results_cloud = clustering_reference_creation.create(
    #         frames[0],
    #         frames,
    #         0,
    #         self._camera_reader.intrinsics(),
    #         self._settings,
    #         self.__selected_product,
    #         self._results,
    #         self._results_db,
    #         self.REFERENCE_RESULT_FOLDER,
    #     )

    #     return results_cloud

    def stop(self):
        self._camera_reader.disconnect()
