from dataclasses import dataclass, field
from typing import Dict
from threading import Lock


@dataclass
class SettingsProxy:
    lock: Lock = Lock()
    settings: Dict = field(default_factory=dict)

    def get(self, key: str):
        with self.lock:
            try:
                return self.settings[key]
            except Exception as e:
                print("[Settings Proxy] Failed to get key, doesn't exist. KEY: " + key)

    def set(self, key: str, value):
        with self.lock:
            self.settings[key] = value

    def get_settings(self) -> Dict:
        return self.settings

    def load(self, settings: Dict[str, str]) -> None:
        with self.lock:
            for key, value in settings.items():
                self.settings[key] = value
