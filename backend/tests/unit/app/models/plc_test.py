from app.models.plc import (
    Plc,
    PlcCreate,
    PlcDelete,
    PlcUpdate,
    PlcRead,
)


def test_plc_from_orm_create():
    expected = PlcCreate()
    result = Plc.from_orm(expected)
    assert result.ip == expected.ip


def test_plc_from_orm_delete():
    expected = PlcDelete()
    result = Plc.from_orm(expected)
    assert result.ip == expected.ip


def test_plc_from_orm_update():
    expected = PlcUpdate()
    result = Plc.from_orm(expected)
    assert result.ip == expected.ip


def test_plc_from_orm_read():
    expected = PlcRead()
    result = Plc.from_orm(expected)
    assert result.ip == expected.ip
