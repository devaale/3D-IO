class MillimetersConvertor:
    @classmethod
    def to_meters(self, value: float) -> float:
        return float(value / 1000)

    @classmethod
    def from_meters(self, value: float) -> float:
        return round(float(value * 1000), 5)
