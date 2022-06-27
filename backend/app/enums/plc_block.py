from enum import auto
from app.enums.base import AutoNameEnum


class PlcBlockDataType(str, AutoNameEnum):
    BOOL = auto()
    BYTE = auto()
    WORD = auto()
    DWORD = auto()
    INT = auto()
    DINT = auto()
    LINT = auto()
    REAL = auto()
    TIME = auto()
    DATE = auto()
    TIME_OF_DAY = auto()
    CHAR = auto()
    DATE_TIME = auto()


class PlcBlockByteSize:
    BOOL = 1
    BYTE = 1
    WORD = 2
    DWORD = 4
    INT = 2
    DINT = 4
    LINT = 8
    REAL = 4
    TIME = 4
    DATE = 2
    TIME_OF_DAY = 4
    CHAR = 1
    DATE_TIME = 12


class PlcBlockMode(str, AutoNameEnum):
    READ = auto()
    WRITE = auto()


class PlcBlockCommand(str, AutoNameEnum):
    PRODUCT = auto()

    TRIGGER = auto()
    LEARN_MODE = auto()

    RESULT = auto()
    PROCESSING_DONE = auto()

    CONNECTED = auto()
    MODEL_EXIST = auto()
