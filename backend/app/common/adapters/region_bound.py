from typing import List
from app.common.helpers import math
from app.enums.region import RegionPosition


class RegionBoundAdapter:
    @classmethod
    def get_bounds_x(
        cls,
        position: str,
        size: float,
        cloud_min_x: float,
        cloud_max_x: float,
    ) -> List[float]:

        if (
            position == RegionPosition.LEFT_BOT.value
            or position == RegionPosition.LEFT_TOP
        ):
            min_x = cloud_min_x
            max_x = math.fraction(cloud_min_x, cloud_max_x, size)
        elif (
            position == RegionPosition.RIGHT_BOT or position == RegionPosition.RIGHT_TOP
        ):
            min_x = math.fraction(cloud_max_x, cloud_min_x, size)
            max_x = cloud_max_x
        else:
            min_x = cloud_min_x
            max_x = cloud_max_x

        return min_x, max_x

    @classmethod
    def get_bounds_y(
        cls, position: str, size: float, cloud_min_y: float, cloud_max_y: float
    ):

        if (
            position == RegionPosition.LEFT_BOT.value
            or position == RegionPosition.RIGHT_BOT
        ):
            min_y = cloud_min_y
            max_y = math.fraction(cloud_min_y, cloud_max_y, size)
        elif (
            position == RegionPosition.LEFT_TOP.value
            or position == RegionPosition.RIGHT_TOP
        ):
            min_y = math.fraction(cloud_max_y, cloud_min_y, size)
            max_y = cloud_max_y
        else:
            min_y = cloud_min_y
            max_y = cloud_max_y

        return min_y, max_y
