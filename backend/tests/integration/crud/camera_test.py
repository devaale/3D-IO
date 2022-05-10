from app.models.camera import CameraCreate
from app.crud.camera import CameraCRUD
import pytest
from app.database.session import connect_test_db, ScopedSessionTest


@pytest.mark.asyncio
async def test_camera_create():
    await connect_test_db()
    expected = CameraCreate()

    async with ScopedSessionTest() as session:
        expected = CameraCreate()
        result = await CameraCRUD().add(data=expected, session=session)

    assert expected.serial_num == result.serial_num


@pytest.mark.asyncio
async def test_camera_get():
    await connect_test_db()
    expected = CameraCreate()

    async with ScopedSessionTest() as session:
        _ = await CameraCRUD().add(data=expected, session=session)
        result = await CameraCRUD().get(session=session)

    assert result.serial_num == expected.serial_num
