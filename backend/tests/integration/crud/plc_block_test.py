from numpy import block
from app.models.plc import PlcCreate, Plc
from app.models.plc_block import PlcBlockCreate, PlcBlock
from app.crud.plc import CRUDPlc
from app.crud.plc_block import CRUDPlcBlock
import pytest

from app.database.session import connect_test_db, ScopedSessionTest


@pytest.mark.asyncio
async def test_plc_block_create():
    await connect_test_db()

    async with ScopedSessionTest() as session:
        plc_block = await CRUDPlc().add(data=PlcBlockCreate(), session=session)
    assert plc_block is not None


@pytest.mark.asyncio
async def test_plc_block_get():
    await connect_test_db()

    async with ScopedSessionTest() as session:
        _ = await CRUDPlcBlock().add(data=PlcBlockCreate(), session=session)
        plc_block = await CRUDPlcBlock().get(id=1, session=session)
    assert plc_block is not None


@pytest.mark.asyncio
async def test_plc_block_get_all():
    await connect_test_db()
    count = 0
    async with ScopedSessionTest() as session:
        _ = await CRUDPlcBlock().add(data=PlcBlockCreate(), session=session)
        _ = await CRUDPlcBlock().add(data=PlcBlockCreate(), session=session)
        _ = await CRUDPlcBlock().add(data=PlcBlockCreate(), session=session)

        blocks = await CRUDPlcBlock().get_all(session=session)
        count = len(blocks)
    assert count == 3


@pytest.mark.asyncio
async def test_plc_block_delete():
    await connect_test_db()

    async with ScopedSessionTest() as session:
        added = await CRUDPlcBlock().add(data=PlcBlockCreate(), session=session)
        deleted = await CRUDPlcBlock().delete(data=added, session=session)
    assert deleted is None
