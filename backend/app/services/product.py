from app.models.product import Product
from app.crud.product import ProductCRUD


class CurrentProductService:
    def __init__(self) -> None:
        pass

    async def get_current(self) -> Product:
        current = await ProductCRUD().get_current()

        return current
