import os
import time
import json
import pyrealsense2 as rs

from app.common.interfaces.camera.reader import CameraReader
from hardware.camera.real_sense.data import RealSenseData


class RealSenseD435Reader(CameraReader):
    CONFIG_LOAD_TIME = 5
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
    CONFIG_PATH = CURRENT_DIR + "\\" + "config.json"

    def __init__(self, width: int, height: int, fps: int, serial_num: str):
        self._fps = fps
        self._width = width
        self._height = height
        self._serial_num = serial_num

        self._camera = None
        self._pipeline = None
        self._config = rs.config()
        self._context = rs.context()

    async def read(self, frame_count: int) -> RealSenseData:

        depth_frames = []
        color_frames = []

        for _ in range(frame_count):
            try:
                frames = self._pipeline.wait_for_frames()
            except Exception as error:
                print("Camera exception occurred: {}".format(error))
                continue

            color_frame = frames.get_color_frame()
            depth_frame = frames.get_depth_frame()

            depth_frames.append(depth_frame)
            color_frames.append(color_frame)

        return RealSenseData(depth_frames, color_frames, self._intrinsics())

    async def connect(self) -> bool:
        camera = await self._find_camera()

        _ = await self._configure(camera)

        self._pipeline = await self._enable(camera)

        return True

    async def disconnect(self) -> bool:
        self._pipeline.stop()
        return True

    async def _find_camera(self) -> rs.device:
        serials = await self._get_serials()

        index = serials.index(self._serial_num)

        return self._context.devices[index]

    async def _get_serials(self):
        return [x.get_info(rs.camera_info.serial_number) for x in rs.context().devices]

    async def _configure(self, camera: rs.device) -> None:
        config = await self._read_config(self.CONFIG_PATH)

        mode = rs.rs400_advanced_mode(camera)

        mode.toggle_advanced_mode(True)

        time.sleep(self.CONFIG_LOAD_TIME)

        mode.load_json(config)

    async def _enable(self, camera: rs.device) -> rs.pipeline:
        pipeline = rs.pipeline(self._context)

        serial = camera.get_info(rs.camera_info.serial_number)

        self._config.enable_device(serial)

        await self._enable_stream(rs.stream.depth, rs.format.z16)
        await self._enable_stream(rs.stream.color, rs.format.bgr8)

        pipeline.start(self._config)
        return pipeline

    async def _read_config(self, path: str) -> str:
        json_dict = {}
        with open(path) as file:
            for key, value in json.load(file).items():
                json_dict[key] = value

        return str(json_dict).replace("'", '"')

    async def _enable_stream(self, stream: rs.stream, format: rs.format):
        self._config.enable_stream(stream, self._width, self._height, format, self._fps)

    def _intrinsics(self) -> rs.intrinsics:
        stream = self._pipeline.get_active_profile().get_stream(rs.stream.depth)

        instrinsics = stream.as_video_stream_profile().get_intrinsics()

        return instrinsics
