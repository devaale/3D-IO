from typing import List

from fastapi import APIRouter, HTTPException
from app.crud.setting import CRUDSetting
from app.models.setting import Setting, SettingCreate

router = APIRouter()


@router.post("/settings", response_model=Setting)
async def post(data: SettingCreate):
    return await CRUDSetting().add(data=data)


@router.get("/settings/{id}", response_model=Setting)
async def get(id: int):
    data = await CRUDSetting().get(id=id)

    if not data:
        raise HTTPException(status_code=404, detail="Setting not found")

    return data


@router.delete("/settings/{id}", response_model=Setting)
async def delete(id: int):
    data = await CRUDSetting().get(id=id)

    if not data:
        raise HTTPException(status_code=404, detail="Setting not found")

    return await CRUDSetting().delete(data=data)


@router.get("/settings", response_model=List[Setting])
async def get_all():
    return await CRUDSetting().get_all()
