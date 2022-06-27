from app.models.product import ProductCreate, Product
from app.crud.product import ProductCRUD
import pytest

from app.database.session import connect_test_db, ScopedSessionTest


@pytest.mark.asyncio
async def test_product_create():
    await connect_test_db()
    expected = ProductCreate()

    async with ScopedSessionTest() as session:
        expected = ProductCreate()
        result = await ProductCRUD().create(data=expected, session=session)

    assert expected.model == result.model


@pytest.mark.asyncio
async def test_product_get():
    await connect_test_db()
    expected = ProductCreate()

    async with ScopedSessionTest() as session:
        _ = await ProductCRUD().create(data=expected, session=session)
        result = await ProductCRUD().get(id=1, session=session)

    assert result.model == expected.model


@pytest.mark.asyncio
async def test_product_get_all():
    await connect_test_db()
    add = ProductCreate()
    count = 0
    async with ScopedSessionTest() as session:
        _ = await ProductCRUD().create(data=add, session=session)
        _ = await ProductCRUD().create(data=add, session=session)
        _ = await ProductCRUD().create(data=add, session=session)
        result = await ProductCRUD().get_all(session=session)
        count = len(result)
    assert count == 3


@pytest.mark.asyncio
async def test_product_get_current():
    await connect_test_db()
    add = ProductCreate(current=True)
    result = None
    async with ScopedSessionTest() as session:
        _ = await ProductCRUD().create(data=add, session=session)
        result = await ProductCRUD().get_current(session=session)
    assert add.model == result.model


@pytest.mark.asyncio
async def test_product_delete():
    await connect_test_db()
    add = ProductCreate()
    async with ScopedSessionTest() as session:
        data = await ProductCRUD().create(data=add, session=session)
        delete = Product(id=data.id)
        _ = await ProductCRUD().delete(data=delete, session=session)

        assert delete.id == 1
