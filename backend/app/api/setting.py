from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_session
from app.crud.setting import CRUDSetting
from app.models.setting import Setting, SettingCreate

router = APIRouter()


# TODO: ADD Detail Messages
@router.post("/settings", response_model=Setting)
async def settings_add(
    data: SettingCreate, session: AsyncSession = Depends(get_session)
):
    return await CRUDSetting.add(session=session, data=data)


@router.get("/settings/{id}", response_model=Setting)
async def settings_get(id: int, session: AsyncSession = Depends(get_session)):
    data = await CRUDSetting.get(session=session)

    if not data:
        raise HTTPException(status_code=404, detail="PLC not found")

    return data


@router.delete("/settings/{id}", response_model=Setting)
async def settings_delete(id: int, session: AsyncSession = Depends(get_session)):
    data = await CRUDSetting.get(session=session)

    if not data:
        raise HTTPException(status_code=404, detail="PLC not found")

    return await CRUDSetting.delete(session=session, data=data)


@router.get("/settings", response_model=List[Setting])
async def settings_get_all(session: AsyncSession = Depends(get_session)):
    return await CRUDSetting.get_all(session=session)
