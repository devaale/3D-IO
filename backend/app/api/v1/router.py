from fastapi import APIRouter

from app.api.v1.controllers import plc, plc_block, setting

router = APIRouter()
router.include_router(plc.router)
router.include_router(plc_block.router)
router.include_router(setting.router)
