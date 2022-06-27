from app.models.position import (
    PositionModel,
    PositionModelCreate,
    PositionModelDelete,
    PositionModelUpdate,
    PositionDetected,
)


def test_position_from_orm_create():
    expected = PositionModelCreate()
    result = PositionModel.from_orm(expected)
    assert result.row == expected.row


def test_position_from_orm_delete():
    expected = PositionModelDelete()
    result = PositionModel.from_orm(expected)
    assert result.row == expected.row


def test_position_from_orm_update():
    expected = PositionModelUpdate()
    result = PositionModel.from_orm(expected)
    assert result.row == expected.row


def test_position_from_orm_detected():
    expected = PositionDetected()
    result = PositionModel.from_orm(expected)
    assert result.row == expected.row
