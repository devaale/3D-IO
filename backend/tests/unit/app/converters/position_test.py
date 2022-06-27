from backend.app.common.converters import position


def test_to_cell_position():
    row, col = position.PositionConverter.to_cell_position(1, 3)
    assert row == 0
    assert col == 1


def test_to_cell_position_zero_test():
    expected = 0
    row, col = position.PositionConverter.to_cell_position(0, 0)
    assert row == expected
    assert col == expected
