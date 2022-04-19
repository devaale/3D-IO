from distutils.log import error
from typing import Tuple


class AngleValidator:
    def __init__(self, threshold: float) -> None:
        self._threshold = threshold

    def validate(self, model_angle: float, detected_angle: float) -> Tuple[bool, float]:
        error = abs(model_angle - detected_angle)

        valid = True if error <= self._threshold else False

        return valid, error
