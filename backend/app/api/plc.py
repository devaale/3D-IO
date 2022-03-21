from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.plc import CRUDPlc
from app.models.plc import Plc, PlcCreate

from app.database.session import get_session

router = APIRouter()

# TODO: ADD Detail Messages
@router.post("/plcs", response_model=Plc)
async def plcs_add(data: PlcCreate, session: AsyncSession = Depends(get_session)):
    exists = await CRUDPlc.exists(session=session)

    if exists:
        raise HTTPException(status_code=409, detail="PLC already exists")

    return await CRUDPlc.add(session=session, data=data)


@router.get("/plcs/{id}", response_model=Plc)
async def plcs_get(id: int, session: AsyncSession = Depends(get_session)):
    data = await CRUDPlc.get(session=session)

    if not data:
        raise HTTPException(status_code=404, detail="PLC not found")

    return data


@router.delete("/plcs/{id}", response_model=Plc)
async def plcs_delete(id: int, session: AsyncSession = Depends(get_session)):
    data = await CRUDPlc.get(session=session)

    if not data:
        raise HTTPException(status_code=404, detail="PLC not found")

    return await CRUDPlc.delete(session=session, data=data)
