class PrecentageConvertor:
    @classmethod
    def to_fraction(self, value: float) -> float:
        return float(value / 100)

    @classmethod
    def from_fraction(self, value: float) -> float:
        return float(value * 100)
