import snap7
from typing import Any
from threading import Lock


class PlcReader:
    def __init__(self, ip: str, rack: int, slot: int):
        self._ip = ip
        self._rack = rack
        self._slot = slot
        self._lock = Lock()
        self._client = snap7.client.Client()

    def connect(self) -> bool:
        with self._lock:
            try:
                self._client.connect(self._ip, self._rack, self._slot)
            except Exception:
                return self.connected()

    def disconnect(self) -> bool:
        with self._lock:
            try:
                self._client.disconnect()
            except Exception:
                return self.connected()

    def connected(self) -> bool:
        with self._lock:
            try:
                return self._client.get_connected()
            except Exception:
                return False

    def read(self, db_num: int, offset: int, offset_bit: int, size: int) -> Any:
        pass

    def write(self, db_num: int, offset: int, offset_bit: int, size: int, value: Any):
        pass
