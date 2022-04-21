from typing import List

from app.crud.plc_block import CRUDPlcBlock
from fastapi import APIRouter, HTTPException, Depends
from app.models.plc_block import PlcBlock, PlcBlockCreate
from app.database.session import get_session
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.post("/plc-blocks", response_model=PlcBlock)
async def post(data: PlcBlockCreate, session: AsyncSession = Depends(get_session)):
    return await CRUDPlcBlock().add(data=data, session=session)


@router.get("/plc-blocks/{id}", response_model=PlcBlock)
async def get(id: int, session: AsyncSession = Depends(get_session)):
    data = await CRUDPlcBlock().get(id=id, session=session)

    if not data:
        raise HTTPException(status_code=404, detail="PLC block not found")

    return data


@router.delete("/plc-blocks/{id}", response_model=PlcBlock)
async def delete(id: int, session: AsyncSession = Depends(get_session)):
    data = await CRUDPlcBlock().get(id=id, session=session)

    if not data:
        raise HTTPException(status_code=404, detail="PLC block not found")

    return await CRUDPlcBlock().delete(data=data)


@router.get("/plc-blocks", response_model=List[PlcBlock])
async def get_all(session: AsyncSession = Depends(get_session)):
    return await CRUDPlcBlock().get_all(session=session)
