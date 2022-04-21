from typing import Tuple
from app.common.converters.millimeters import MillimetersConvertor


class DepthValidator:
    def __init__(self) -> None:
        pass

    def validate(
        self, model_depth: float, detected_depth: float, threshold: float
    ) -> bool:
        error = abs(model_depth - detected_depth)

        error_mm = MillimetersConvertor.from_meters(error)

        valid = True if error <= threshold else False

        return valid, error_mm
