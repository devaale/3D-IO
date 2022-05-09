from backend.app.database.sql_session import AsyncSQLSessionProxy
from backend.app.models.product import ProductCreate
from backend.app.crud.product import ProductCRUD
import pytest


@pytest.mark.asyncio
async def test_plc_create():
    expected = ProductCreate()
    session = AsyncSQLSessionProxy().get()
    async with session:
        result = await ProductCRUD().add(data=expected, session=session)
    assert result.model == expected.model


@pytest.mark.asyncio
async def test_plc_get():
    expected = ProductCreate()
    session = AsyncSQLSessionProxy().get()
    async with session:
        _ = await ProductCRUD().add(data=expected, session=session)
        result = await ProductCRUD().get(session=session)
    assert result.model == expected.model


@pytest.mark.asyncio
async def test_plc_delete():
    data = ProductCreate()
    expected = None
    session = AsyncSQLSessionProxy().get()
    async with session:
        expected = await ProductCRUD().add(data=data, session=session)
        result = await ProductCRUD().delete(data=expected, session=session)
    assert result.id == expected.id


@pytest.mark.asyncio
async def test_plc_exist():
    data = ProductCreate()
    expected = True
    session = AsyncSQLSessionProxy().get()
    async with session:
        data = await ProductCRUD().add(data=data, session=session)
        result = await ProductCRUD().exists(data=data.id, session=session)
    assert result == expected
