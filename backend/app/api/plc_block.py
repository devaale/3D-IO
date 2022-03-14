from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session
from app.crud.plc_block import CRUDPlcBlock
from app.models.plc_block import PlcBlock, PlcBlockCreate

router = APIRouter()

# TODO: Check correctness of the API's
@router.post("/plc-blocks", response_model=PlcBlock)
async def add_plc_block(setting: PlcBlockCreate, session: AsyncSession = Depends(get_session)):
    return await CRUDPlcBlock.add(session=session, setting=setting)

@router.delete("/plc-blocks/{id}", response_model=PlcBlock)
async def delete_plc_block(id, session: AsyncSession = Depends(get_session)):
    return await CRUDPlcBlock.delete(session, id)

@router.get("/plc-blocks/{plc-id}", response_model=List[PlcBlock])
async def get_plc_blocks_by_plc(plc_id, session: AsyncSession = Depends(get_session)):
    return await CRUDPlcBlock.get_all_by_plc(session=session, plc_id=plc_id)
