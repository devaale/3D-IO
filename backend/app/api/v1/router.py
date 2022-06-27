from fastapi import APIRouter

from app.api.v1.controllers import setting

router = APIRouter()
router.include_router(setting.router)
