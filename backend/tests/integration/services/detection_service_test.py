from app.services.detection import DetectionService
import pytest


@pytest.mark.asyncio
async def test_detection_error_no_input():
    service = DetectionService(None, None, None)
    with pytest.raises(Exception):
        _ = await service.detect(None, None)
