from app.models.plc_block import (
    PlcBlock,
    PlcBlockCreate,
    PlcBlockDelete,
    PlcBlockUpdate,
    PlcBlockRead,
)


def test_plc_block_from_orm_create():
    expected = PlcBlockCreate()
    result = PlcBlock.from_orm(expected)
    assert result.command == expected.command


def test_plc_block_from_orm_delete():
    expected = PlcBlockDelete()
    result = PlcBlock.from_orm(expected)
    assert result.command == expected.command


def test_plc_block_from_orm_update():
    expected = PlcBlockUpdate()
    result = PlcBlock.from_orm(expected)
    assert result.command == expected.command


def test_plc_block_from_orm_read():
    expected = PlcBlockRead()
    result = PlcBlock.from_orm(expected)
    assert result.command == expected.command
