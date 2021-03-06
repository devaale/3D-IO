from typing import List

from fastapi import APIRouter, HTTPException, Depends
from app.crud.setting import CRUDSetting
from app.models.setting import Setting, SettingCreate
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_session

router = APIRouter()


@router.post("/settings", response_model=Setting)
async def post(data: SettingCreate, session: AsyncSession = Depends(get_session)):
    return await CRUDSetting().add(data=data, session=session)


@router.get("/settings/{id}", response_model=Setting)
async def get(id: int, session: AsyncSession = Depends(get_session)):
    data = await CRUDSetting().get(id=id, session=session)

    if not data:
        raise HTTPException(status_code=404, detail="Setting not found")

    return data


@router.delete("/settings/{id}", response_model=Setting)
async def delete(id: int, session: AsyncSession = Depends(get_session)):
    data = await CRUDSetting().get(id=id, session=session)

    if not data:
        raise HTTPException(status_code=404, detail="Setting not found")

    return await CRUDSetting().delete(data=data, session=session)


@router.get("/settings", response_model=List[Setting])
async def get_all(session: AsyncSession = Depends(get_session)):
    return await CRUDSetting().get_all(session=session)
