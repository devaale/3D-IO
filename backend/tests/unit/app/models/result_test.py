from app.models.result import (
    Result,
    ResultCreate,
    ResultDelete,
    ResultUpdate,
)


def test_result_from_orm_create():
    expected = ResultCreate()
    result = Result.from_orm(expected)
    assert result.col == expected.col


def test_result_from_orm_delete():
    expected = ResultDelete()
    result = Result.from_orm(expected)
    assert result.col == expected.col


def test_result_from_orm_update():
    expected = ResultUpdate()
    result = Result.from_orm(expected)
    assert result.col == expected.col
