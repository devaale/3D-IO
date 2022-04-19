from app.crud.plc import CRUDPlc
from app.models.plc import Plc, PlcCreate

from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.post("/plcs", response_model=Plc)
async def post(data: PlcCreate):
    exists = await CRUDPlc().exists()

    if exists:
        raise HTTPException(status_code=409, detail="PLC already exists")

    return await CRUDPlc().add(data)


@router.get("/plcs/{id}", response_model=Plc)
async def get(id: int):
    data = await CRUDPlc().get()

    if not data:
        raise HTTPException(status_code=404, detail="PLC not found")

    return data


@router.delete("/plcs/{id}", response_model=Plc)
async def delete(id: int):
    data = await CRUDPlc().get()

    if not data:
        raise HTTPException(status_code=404, detail="PLC not found")

    return await CRUDPlc().delete(data=data)
