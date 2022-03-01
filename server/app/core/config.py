import os
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
