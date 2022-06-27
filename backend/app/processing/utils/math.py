import numpy as np
from typing import List


def fraction(from_point, to_point, fraction_size) -> float:
    return from_point * (1 - fraction_size) + to_point * fraction_size


def calculate_mean_by_axis(data: List[List[float]], axis: int):
    mean = np.mean(data, axis=0)[axis]
    return mean
