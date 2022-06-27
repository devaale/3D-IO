from app.common.interfaces.database.session_proxy import SessionProxy
from app.crud.position import PositionModelCRUD
from app.crud.region import RegionModelCRUD

class ModelService:
    def __init__(self, session_proxy: SessionProxy) -> None:
        self._session_proxy = session_proxy
    
    async def get_position_model(self, row: int, col: int, product_id: int):
        session_scoped = self._session_proxy.get()

        async with session_scoped as session:
            model = await PositionModelCRUD().find_by_position_and_product(
                row, col, product_id, session
            )
            
            return model
            
    
    async def get_region_model(self, position: str, position_model_id: int):
        session_scoped = self._session_proxy.get()

        async with session_scoped as session:
            model = (
                await RegionModelCRUD().find_by_position_and_position_model(
                    position, position_model_id, session
                )
            )
            
            return model
            