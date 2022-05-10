from backend.app.processing.utils import math


def test_fraction():
    result = math.fraction(0, 1, 0.5)
    assert result == 0.5


def test_calculate_mean_axis():
    result = math.calculate_mean_by_axis([[1, 1, 1], [1, 1, 1]], 0)
    assert result == 1
