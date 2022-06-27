from app.models.plc import PlcCreate, Plc
from app.crud.plc import CRUDPlc
import pytest

from app.database.session import connect_test_db, ScopedSessionTest


@pytest.mark.asyncio
async def test_plc_create():
    await connect_test_db()
    expected = PlcCreate()

    async with ScopedSessionTest() as session:
        expected = PlcCreate()
        result = await CRUDPlc().add(data=expected, session=session)

    assert expected.ip == result.ip


@pytest.mark.asyncio
async def test_plc_get():
    await connect_test_db()
    expected = PlcCreate()

    async with ScopedSessionTest() as session:
        _ = await CRUDPlc().add(data=expected, session=session)
        result = await CRUDPlc().get(id=1, session=session)

    assert result.ip == expected.ip


@pytest.mark.asyncio
async def test_plc_delete():
    await connect_test_db()
    expected = PlcCreate()
    async with ScopedSessionTest() as session:
        data = await CRUDPlc().add(data=expected, session=session)
        delete = Plc(id=data.id)
        _ = await CRUDPlc().delete(data=delete, session=session)

        assert delete.id == 1


@pytest.mark.asyncio
async def test_plc_exists_true():
    await connect_test_db()
    expected = PlcCreate()

    async with ScopedSessionTest() as session:
        expected = PlcCreate()
        _ = await CRUDPlc().add(data=expected, session=session)
        exists = await CRUDPlc().exists(id=1, session=session)
    assert exists == True


@pytest.mark.asyncio
async def test_plc_exists_true():
    await connect_test_db()

    async with ScopedSessionTest() as session:
        exists = await CRUDPlc().exists(id=1, session=session)
    assert exists == False
