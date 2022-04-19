from enum import auto
from app.enums.base import AutoNameEnum


class RegionPosition(str, AutoNameEnum):
    LEFT_BOT = auto()
    LEFT_TOP = auto()
    RIGHT_TOP = auto()
    RIGHT_BOT = auto()
