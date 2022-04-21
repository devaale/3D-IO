from turtle import color


class CameraData:
    def __init__(self, depth_data=None, color_data=None, intrinsics=None) -> None:
        self.depth_data = depth_data
        self.color_data = color_data
        self.intrinsics = intrinsics
