from app.services.product import CurrentProductService
from app.models.position import PositionDetected
from app.crud.position import PositionModelCRUD
from typing import List

from app.enums.model import ModelAction
from app.models.position import PositionModelCreate


class ResultService:
    def __init__(self, model_action: ModelAction) -> None:
        self._model_action = ModelAction.TRAIN.value
        self._product_service = CurrentProductService()

    async def handle_detection(self, detection: PositionDetected):

        if self._model_action == ModelAction.TRAIN.value:
            await self.save_as_model(detection)
        elif self._model_action == ModelAction.PREDICT.value:
            print(f"THIS IS PREDDDDDDDDICTION: {detection}")

    async def save_as_model(self, detection: PositionDetected):
        product = await self._product_service.get_current()

        position_model = await PositionModelCRUD().find_by_position_and_product(
            detection.row, detection.col, product.id
        )

        print(f"THIS IS DETEEEEEEEEEECTION objeeeeeeeeeeeeeeeeeeeects: {detection}")

        if position_model is None:
            # _ = PositionModelCRUD().add(
            #     PositionModelCreate(
            #         position_model.row, position_model.col, 0, product.id
            #     )
            # )
            print("Position model is None :P")
        else:
            print("Position model is not NOOOOONEEEeeeeeeeeeeeeeeeeeeeeeeeeeee :) :P")
