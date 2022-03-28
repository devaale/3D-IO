import os
from typing import List, Optional
from pydantic import BaseSettings

basedir = os.path.abspath(os.path.dirname(__file__))


class Settings(BaseSettings):
    HOST: str = "127.0.0.1"
    PORT: int = 5050
    SCHEMA: str = "http://"
    SOCKET_MOUNT: str = "/"
    SOCKET_CORS_ALLOWED: str = "*"
    SOCKET_ASYNC_MODE: str = "asgi"
    ASGI_PROTOCOL: str = "main:app"
    ASGI_RELOAD: bool = False
    CORS_ALLOWED_ORIGINS: List[str] = []
    ORIGINS: List[str] = ["http://localhost:3001"]
    API_V1_STR: str = "/api/v1"
