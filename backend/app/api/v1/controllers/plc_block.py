from typing import List

from app.crud.plc_block import CRUDPlcBlock
from fastapi import APIRouter, HTTPException
from app.models.plc_block import PlcBlock, PlcBlockCreate

router = APIRouter()


@router.post("/plc-blocks", response_model=PlcBlock)
async def post(data: PlcBlockCreate):
    return await CRUDPlcBlock().add(data=data)


@router.get("/plc-blocks/{id}", response_model=PlcBlock)
async def get(id: int):
    data = await CRUDPlcBlock().get(id=id)

    if not data:
        raise HTTPException(status_code=404, detail="PLC block not found")

    return data


@router.delete("/plc-blocks/{id}", response_model=PlcBlock)
async def delete(id: int):
    data = await CRUDPlcBlock().get(id=id)

    if not data:
        raise HTTPException(status_code=404, detail="PLC block not found")

    return await CRUDPlcBlock().delete(data=data)


@router.get("/plc-blocks", response_model=List[PlcBlock])
async def get_all():
    return await CRUDPlcBlock().get_all()
