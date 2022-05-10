from app.models.camera import (
    Camera,
    CameraCreate,
    CameraDelete,
    CameraUpdate,
    CameraRead,
)


def test_plc_from_orm_create():
    expected = CameraCreate()
    result = Camera.from_orm(expected)
    assert result.type == expected.type


def test_plc_from_orm_delete():
    expected = CameraDelete()
    result = Camera.from_orm(expected)
    assert result.type == expected.type


def test_plc_from_orm_update():
    expected = CameraUpdate()
    result = Camera.from_orm(expected)
    assert result.type == expected.type


def test_plc_from_orm_read():
    expected = CameraRead()
    result = Camera.from_orm(expected)
    assert result.type == expected.type
