import asyncio
from app.services.core import CoreService
from app.database.sql_session import AsyncSQLSessionProxy


class ServiceManager:
    def __init__(self) -> None:
        self._created = False
        self._core_task = None

        self._session_proxy = AsyncSQLSessionProxy()
        self._core_service = CoreService(self._session_proxy)

    async def camera_start(self):
        if not self._created:
            self._core_task = asyncio.create_task(self._core_service.start())
            self._created = True

    async def camera_detect(self):
        await self._core_service.manual_detection()
