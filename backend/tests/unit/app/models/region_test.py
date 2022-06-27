from app.models.region import (
    RegionModel,
    RegionDetected,
    RegionModelCreate,
    RegionModelUpdate,
)


def test_region_from_orm_create():
    expected = RegionModelCreate()
    result = RegionModel.from_orm(expected)
    assert result.position == expected.position


def test_region_from_orm_update():
    expected = RegionModelUpdate()
    result = RegionModel.from_orm(expected)
    assert result.position == expected.position


def test_region_from_orm_detected():
    expected = RegionDetected()
    result = RegionModel.from_orm(expected)
    assert result.position == expected.position
