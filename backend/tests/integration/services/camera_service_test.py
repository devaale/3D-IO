from app.services.camera import CameraService
from hardware.camera.real_sense.d435.reader import RealSenseD435Reader
import pytest


@pytest.mark.asyncio
async def test_camera_start_error():
    service = CameraService()
    with pytest.raises(Exception):
        await service.start()


@pytest.mark.asyncio
async def test_camera_stop_error():
    service = CameraService()
    with pytest.raises(Exception):
        await service.stop()


@pytest.mark.asyncio
async def test_camera_read_error():
    service = CameraService()
    with pytest.raises(Exception):
        await service.stop()


@pytest.mark.asyncio
async def test_camera_read_error():
    service = CameraService()
    result = await service.configure(RealSenseD435Reader(100, 100, 100, "0"))
    assert result == True
