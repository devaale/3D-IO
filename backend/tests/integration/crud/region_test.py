from cv2 import add
from app.models.region import RegionModel
from app.crud.region import RegionModelCRUD

import pytest
from app.database.session import connect_test_db, ScopedSessionTest


@pytest.mark.asyncio
async def test_region_create():
    await connect_test_db()

    async with ScopedSessionTest() as session:
        added = await RegionModelCRUD().add(data=RegionModel(), session=session)

    assert added is not None


@pytest.mark.asyncio
async def test_region_get():
    await connect_test_db()

    async with ScopedSessionTest() as session:
        _ = await RegionModelCRUD().add(data=RegionModel(), session=session)
        region = await RegionModelCRUD().get(id=1, session=session)
    assert region is not None


@pytest.mark.asyncio
async def test_region_get_all():
    await connect_test_db()
    count = 0
    async with ScopedSessionTest() as session:
        _ = await RegionModelCRUD().add(data=RegionModel(), session=session)
        _ = await RegionModelCRUD().add(data=RegionModel(), session=session)
        _ = await RegionModelCRUD().add(data=RegionModel(), session=session)

        regions = await RegionModelCRUD().get_all(session=session)
        count = len(regions)

    assert count is not None


@pytest.mark.asyncio
async def test_region_delete():
    await connect_test_db()
    async with ScopedSessionTest() as session:
        added = await RegionModelCRUD().add(data=RegionModel(), session=session)
        deleted = await RegionModelCRUD().delete(data=added, session=session)

    assert deleted is None


@pytest.mark.asyncio
async def test_region_update():
    await connect_test_db()
    async with ScopedSessionTest() as session:
        added = await RegionModelCRUD().add(data=RegionModel(), session=session)
        added.depth_mean = 10
        updated = await RegionModelCRUD().update(data=added, session=session)

    assert updated.depth_mean == 10


@pytest.mark.asyncio
async def test_region_find_by_position_and_model_none():
    await connect_test_db()
    async with ScopedSessionTest() as session:
        _ = await RegionModelCRUD().add(data=RegionModel(), session=session)
        found = await RegionModelCRUD().find_by_position_and_position_model(
            position="", position_model_id=1, session=session
        )

    assert found is None
