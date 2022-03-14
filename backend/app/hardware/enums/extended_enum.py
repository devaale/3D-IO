from enum import Enum


class ExtendedEnum(Enum):
    @classmethod
    def get_values(cls):
        return list(map(lambda c: c.value, cls))
