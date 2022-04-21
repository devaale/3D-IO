from app.models.product import Product
from app.crud.product import ProductCRUD
from asyncio import Lock

from app.common.interfaces.session_proxy import SessionProxy


class CurrentProductService:
    def __init__(self, session_proxy: SessionProxy) -> None:
        self._lock = Lock()
        self._session_proxy = session_proxy

    async def get_current(self) -> Product:
        async with self._lock:
            session_scoped = self._session_proxy.get()

            async with session_scoped as session:
                current = await ProductCRUD().get_current(session=session)

                return current
