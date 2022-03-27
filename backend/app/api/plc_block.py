from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_session

from app.crud.plc_block import CRUDPlcBlock
from app.models.plc_block import PlcBlock, PlcBlockCreate

router = APIRouter()


@router.post("/plc-blocks", response_model=PlcBlock)
async def post(data: PlcBlockCreate, session: AsyncSession = Depends(get_session)):
    return await CRUDPlcBlock.add(session=session, data=data)


@router.get("/plc-blocks/{id}", response_model=PlcBlock)
async def get(id: int, session: AsyncSession = Depends(get_session)):
    data = await CRUDPlcBlock.get(session=session, id=id)

    if not data:
        raise HTTPException(status_code=404, detail="PLC block not found")

    return data


@router.delete("/plc-blocks/{id}", response_model=PlcBlock)
async def delete(id: int, session: AsyncSession = Depends(get_session)):
    data = await CRUDPlcBlock.get(session=session, id=id)

    if not data:
        raise HTTPException(status_code=404, detail="PLC block not found")

    return await CRUDPlcBlock.delete(session=session, data=data)


@router.get("/plc-blocks", response_model=List[PlcBlock])
async def get_all(session: AsyncSession = Depends(get_session)):
    return await CRUDPlcBlock.get_all(session=session)
