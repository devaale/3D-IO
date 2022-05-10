from backend.app.common.validators.angle import AngleValidator


def test_angle_valid():
    validator = AngleValidator(1)
    result, error = validator.validate(1, 1)
    assert result is True
    assert error is 0


def test_angle_invalid():
    validator = AngleValidator(1)
    result, error = validator.validate(3, 1)
    assert result is False
    assert error is 2
