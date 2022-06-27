from app.models.position import PositionModelCreate
from app.crud.position import PositionModelCRUD
from app.models.product import ProductCreate
from app.crud.product import ProductCRUD

import pytest

from app.database.session import connect_test_db, ScopedSessionTest


@pytest.mark.asyncio
async def test_position_model_create():
    await connect_test_db()

    async with ScopedSessionTest() as session:
        _ = await ProductCRUD().create(data=ProductCreate(), session=session)
        expected = PositionModelCreate(
            row=0, col=0, plane_angle=0, product_id=1, regions=[]
        )
        result = await PositionModelCRUD().add(data=expected, session=session)

    assert expected.col == result.col
    assert expected.row == result.row


@pytest.mark.asyncio
async def test_position_model_get():
    await connect_test_db()
    async with ScopedSessionTest() as session:
        _ = await ProductCRUD().create(data=ProductCreate(), session=session)
        expected = PositionModelCreate(
            row=0, col=0, plane_angle=0, product_id=1, regions=[]
        )
        _ = await PositionModelCRUD().add(data=expected, session=session)
        result = await PositionModelCRUD().get(id=1, session=session)
    assert expected.col == result.col
    assert expected.row == result.row


@pytest.mark.asyncio
async def test_position_model_get_all():
    await connect_test_db()
    result_count = 0
    async with ScopedSessionTest() as session:
        _ = await ProductCRUD().create(data=ProductCreate(), session=session)
        expected = PositionModelCreate(
            row=0, col=0, plane_angle=0, product_id=1, regions=[]
        )
        _ = await PositionModelCRUD().add(data=expected, session=session)
        _ = await PositionModelCRUD().add(data=expected, session=session)
        _ = await PositionModelCRUD().add(data=expected, session=session)
        result = await PositionModelCRUD().get_all(session=session)
        result_count = len(result)
    assert result_count == 3


@pytest.mark.asyncio
async def test_position_model_delete():
    await connect_test_db()
    async with ScopedSessionTest() as session:
        _ = await ProductCRUD().create(data=ProductCreate(), session=session)
        added = PositionModelCreate(
            row=0, col=0, plane_angle=0, product_id=1, regions=[]
        )
        deleted = await PositionModelCRUD().add(data=added, session=session)
        _ = await PositionModelCRUD().delete(data=deleted, session=session)

        assert deleted.id == 1


@pytest.mark.asyncio
async def test_position_model_find_by_position_and_product():
    await connect_test_db()
    async with ScopedSessionTest() as session:
        _ = await ProductCRUD().create(data=ProductCreate(), session=session)
        added = PositionModelCreate(
            row=0, col=0, plane_angle=0, product_id=1, regions=[]
        )
        _ = await PositionModelCRUD().add(data=added, session=session)
        result = await PositionModelCRUD().find_by_position_and_product(
            row=0, col=0, product_id=1, session=session
        )

        assert result.id == 1
        assert result.col == 0
        assert result.row == 0


@pytest.mark.asyncio
async def test_position_model_update():
    await connect_test_db()
    async with ScopedSessionTest() as session:
        _ = await ProductCRUD().create(data=ProductCreate(), session=session)
        added = PositionModelCreate(
            row=0, col=0, plane_angle=0, product_id=1, regions=[]
        )
        added_position = await PositionModelCRUD().add(data=added, session=session)

        added_position.plane_angle = 10
        updated_position = await PositionModelCRUD().update(
            data=added_position, session=session
        )

        assert updated_position.plane_angle == 10
