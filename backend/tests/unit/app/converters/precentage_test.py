from backend.app.common.converters import precentage


def test_to_fraction():
    expected = 0.1
    result = precentage.PrecentageConvertor.to_fraction(10)
    assert result == expected


def test_from_fraction():
    expected = 10
    result = precentage.PrecentageConvertor.from_fraction(0.1)
    assert result == expected
