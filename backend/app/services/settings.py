from asyncio import Lock
from dataclasses import field
from typing import Any, List
from app.models.setting import Setting
from app.crud.setting import CRUDSetting
from app.common.adapters.settings import SettingsValueAdapter
from app.common.interfaces.database.session_proxy import SessionProxy


class SettingsService:
    def __init__(self, session_proxy: SessionProxy) -> None:
        self._lock = Lock()
        self._session_proxy = session_proxy
        self._settings: List[Setting] = field(default_factory=list)

    async def load(self):
        async with self._lock:
            session_scoped = self._session_proxy.get()

            async with session_scoped as session:
                self._settings = await CRUDSetting().get_all(session=session)

    async def get(self, key: str) -> Any:
        async with self._lock:
            setting = [x for x in self._settings if x.key == key][0]

            if setting is None:
                raise ValueError()

            value = SettingsValueAdapter.adapt(setting)

            return value

    async def set(self, key: str, value):
        async with self._lock:
            self.settings[key] = value
