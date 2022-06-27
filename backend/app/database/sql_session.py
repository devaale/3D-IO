from app.common.interfaces.database.session_proxy import SessionProxy
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import ScopedSession


class AsyncSQLSessionProxy(SessionProxy):
    def get(self) -> AsyncSession:
        return ScopedSession()
