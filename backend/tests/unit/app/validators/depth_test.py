from app.common.validators.depth import DepthValidator


def test_depth_valid():
    validator = DepthValidator()
    result, error = validator.validate(1, 1, 1)
    assert result == True
    assert error == 0


def test_depth_invalid():
    validator = DepthValidator()
    result, error = validator.validate(0.003, 0.001, 0.001)
    assert result == False
    assert error == 2
