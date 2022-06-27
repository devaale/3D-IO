from backend.app.common.converters import millimeters


def test_millimeters_to_meteres():
    expected = 0.001
    result = millimeters.MillimetersConvertor.to_meters(1)
    assert result == expected


def test_millimeters_to_meteres_zero_test():
    result = millimeters.MillimetersConvertor.to_meters(0)
    assert result == 0


def test_millimeters_from_meters():
    expected = 1000
    result = millimeters.MillimetersConvertor.from_meters(1)
    assert result == expected


def test_millimeters_from_meters_zero():
    result = millimeters.MillimetersConvertor.from_meters(0)
    assert result == 0
