from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session
from app.crud.plc import CRUDPlc
from app.models.plc import Plc, PlcCreate

router = APIRouter()

@router.post("/plcs", response_model=Plc)
async def add_plc(setting: PlcCreate, session: AsyncSession = Depends(get_session)):
    return await CRUDPlc.add(session=session, setting=setting)

@router.delete("/plcs/{id}", response_model=Plc)
async def delete_plc(id, session: AsyncSession = Depends(get_session)):
    return await CRUDPlc.delete(session, id)

@router.get("/plcs", response_model=Plc)
async def get_plc(session: AsyncSession = Depends(get_session)):
    return await CRUDPlc.get(session=session)
