from app.services.product import CurrentProductService
from app.models.position import PositionDetected
from app.crud.position import PositionModelCRUD

from app.enums.model import ModelAction
from app.crud.region import RegionModelCRUD
from app.models.region import RegionDetected
from app.common.validators.depth import DepthValidator
from app.crud.result import ResultCRUD
from app.models.result import ResultCreate
from typing import List
from app.services.settings import SettingsService
from app.common.interfaces.session_proxy import SessionProxy
from app.services.model import ModelService
from app.models.region import RegionModel


class ResultService:
    def __init__(self, session_proxy: SessionProxy) -> None:
        self._count = 0
        self._model_action = ModelAction.TRAIN.value
        self._session_proxy = session_proxy
        self._settings_service = SettingsService(session_proxy)
        self._product_service = CurrentProductService(session_proxy)
        self._model_service = ModelService(session_proxy)
        self._depth_validator = DepthValidator()

    async def handle_detection(self, detection: PositionDetected):
        self._model_action = (
            ModelAction.TRAIN.value if self._count < 3 else ModelAction.PREDICT.value
        )

        product = await self._product_service.get_current()

        product_id = product.id

        if self._model_action == ModelAction.TRAIN.value:
            position_model_id = await self.save_position_as_model(detection, product_id)

            for region in detection.regions:
                _ = await self.save_region_as_model(region, position_model_id)

        elif self._model_action == ModelAction.PREDICT.value:

            position_model = await self._model_service.get_position_model(
                detection.row, detection.col, product_id
            )

            for region in detection.regions:

                region_model = await self._model_service.get_region_model(
                    region.position, position_model.id
                )

                _ = await self.save_detection_as_prediction(region, region_model)

        self._count += 1

    async def save_position_as_model(
        self, detection: PositionDetected, product_id: int
    ):

        position_model = await self._model_service.get_position_model(
            detection.row, detection.col, product_id
        )

        if position_model is None:
            detection.product_id = product_id
            session_scoped = self._session_proxy.get()

            async with session_scoped as session:
                position_added = await PositionModelCRUD().add(detection, session)

                return position_added.id

        session_scoped = self._session_proxy.get()

        async with session_scoped as session:
            position_updated = await PositionModelCRUD().update(position_model, session)

            return position_updated.id

    async def save_region_as_model(
        self, region: RegionDetected, position_model_id: int
    ):

        region_model = await self._model_service.get_region_model(
            region.position, position_model_id
        )

        if region_model is None:
            region.position_model_id = position_model_id
            session_scoped = self._session_proxy.get()

            async with session_scoped as session:
                _ = await RegionModelCRUD().add(region, session)

            return

        session_scoped = self._session_proxy.get()

        async with session_scoped as session:
            _ = await RegionModelCRUD().update(region_model, session)

    async def save_detection_as_prediction(
        self, detected_region: RegionDetected, model_region: RegionModel
    ):
        await self._settings_service.load()

        accuracy = await self._settings_service.get("accuracy")

        product = await self._product_service.get_current()

        product_id = product.id

        valid, error = self._depth_validator.validate(
            model_region.depth_mean, detected_region.depth_mean, accuracy
        )

        result = ResultCreate(valid=valid, depth_error=error, product_id=product_id)

        session_scoped = self._session_proxy.get()

        async with session_scoped as session:
            _ = await ResultCRUD().add(result, session)
