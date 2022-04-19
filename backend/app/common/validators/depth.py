from typing import Tuple


class DepthValidator:
    def __init__(self, threshold: float) -> Tuple[bool, float]:
        self._threshold = threshold

    def validate(self, model_depth: float, detected_depth: float) -> bool:
        error = abs(model_depth - detected_depth)

        valid = True if error <= self._threshold else False

        return valid, error
