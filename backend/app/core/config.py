import os
from typing import List
from pydantic import BaseSettings

basedir = os.path.abspath(os.path.dirname(__file__))


class Settings(BaseSettings):
    SOCKET_MOUNT: str = "/"
    SOCKET_ASYNC_MODE: str = "asgi"
    SOCKET_ORIGINS_ALLOWED: List[str] = []
    ORIGINS_ALLOWED: List[str] = ["http://localhost:3000"]
    API_V1_STR: str = "/api/v1"
