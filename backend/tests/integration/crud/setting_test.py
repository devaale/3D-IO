from app.models.setting import SettingCreate
from app.crud.setting import CRUDSetting

import pytest

from app.database.session import connect_test_db, ScopedSessionTest


@pytest.mark.asyncio
async def test_setting_create():
    await connect_test_db()

    async with ScopedSessionTest() as session:
        added = await CRUDSetting().add(data=SettingCreate(), session=session)
        expected = SettingCreate()

    assert expected.measurement == added.measurement


@pytest.mark.asyncio
async def test_setting_get():
    await connect_test_db()

    async with ScopedSessionTest() as session:
        expected = await CRUDSetting().add(data=SettingCreate(), session=session)
        result = await CRUDSetting().get(id=1, session=session)

    assert expected.measurement == result.measurement


@pytest.mark.asyncio
async def test_setting_get_all():
    await connect_test_db()
    result_count = 0
    async with ScopedSessionTest() as session:
        _ = await CRUDSetting().add(data=SettingCreate(), session=session)
        _ = await CRUDSetting().add(data=SettingCreate(), session=session)
        _ = await CRUDSetting().add(data=SettingCreate(), session=session)

        result = await CRUDSetting().get_all(session=session)
        result_count = len(result)

    assert result_count == 3


@pytest.mark.asyncio
async def test_setting_delete():
    await connect_test_db()

    async with ScopedSessionTest() as session:
        deleted = await CRUDSetting().add(data=SettingCreate(), session=session)
        _ = await CRUDSetting().delete(data=deleted, session=session)

        assert deleted.id == deleted.id


@pytest.mark.asyncio
async def test_setting_update_value():
    await connect_test_db()

    async with ScopedSessionTest() as session:
        _ = await CRUDSetting().add(data=SettingCreate(), session=session)
        updated = await CRUDSetting().update_value(id=1, value=10, session=session)

        assert updated.value == 10


@pytest.mark.asyncio
async def test_setting_exists_true():
    await connect_test_db()

    async with ScopedSessionTest() as session:
        _ = await CRUDSetting().add(data=SettingCreate(), session=session)
        exists = await CRUDSetting().exists(id=1, session=session)

        assert exists == True


@pytest.mark.asyncio
async def test_setting_exists_false():
    await connect_test_db()

    async with ScopedSessionTest() as session:
        exists = await CRUDSetting().exists(id=1, session=session)

        assert exists == False
