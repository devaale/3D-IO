from enum import auto
from app.enums.base import AutoNameEnum


class ModelAction(str, AutoNameEnum):
    TRAIN = auto()
    PREDICT = auto()
