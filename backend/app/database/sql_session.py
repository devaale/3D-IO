from app.common.interfaces.session_proxy import SessionProxy
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import ScopedSession
from asyncio import Lock


class AsyncSQLSessionProxy(SessionProxy):
    def __init__(self) -> None:
        self._lock = Lock()

    def get(self) -> AsyncSession:
        return ScopedSession()
