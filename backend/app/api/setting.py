from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session
from app.crud.setting import CRUDSetting
from app.models.setting import Setting, SettingCreate

router = APIRouter()

@router.post("/settings", response_model=Setting)
async def add_setting(setting: SettingCreate, session: AsyncSession = Depends(get_session)):
    return await CRUDSetting.add(session=session, setting=setting)

@router.delete("/settings/{id}", response_model=Setting)
async def delete_setting(id, session: AsyncSession = Depends(get_session)):
    return await CRUDSetting.delete(session, id)

@router.get("/settings", response_model=List[Setting])
async def get_settings(session: AsyncSession = Depends(get_session)):
    return await CRUDSetting.get_all(session=session)
