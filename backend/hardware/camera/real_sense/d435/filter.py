import pyrealsense2 as rs


class CameraFilter:
    @staticmethod
    def apply_temporal_filter(
        frame, smooth_alpha: float = 0.4, smooth_delta: float = 20
    ):
        filter = rs.temporal_filter()

        filter_smooth_alpha = rs.option.filter_smooth_alpha
        filter_smooth_delta = rs.option.filter_smooth_delta

        filter.set_option(filter_smooth_alpha, smooth_alpha)
        filter.set_option(filter_smooth_delta, smooth_delta)

        filtered_frame = filter.process(frame)

        return filtered_frame

    @staticmethod
    def apply_threshold_filter(frame, depth_from: float, depth_to: float):
        filter = rs.threshold_filter()

        filter_min_dist = rs.option.min_distance
        filter_max_dist = rs.option.max_distance

        filter.set_option(filter_min_dist, depth_from)
        filter.set_option(filter_max_dist, depth_to)

        filtered_frame = filter.process(frame)

        return filtered_frame
