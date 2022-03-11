from ..db import get_session
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

#TODO: Check how to avoid relative imports
from fastapi import APIRouter, Depends, HTTPException
from ..models.setting import Setting, SettingCreate, SettingDelete

router = APIRouter()

@router.delete("/settings/{id}", response_model=SettingDelete)
async def delete_setting(id, session: AsyncSession = Depends(get_session)):
    db_setting = await session.get(Setting, id)

    if not db_setting:
        raise HTTPException(status_code=404, detail="Setting not found")
    
    await session.delete(db_setting)
    await session.commit()
    return db_setting


@router.get("/settings", response_model=list[Setting])
async def get_settings(session: AsyncSession = Depends(get_session)):
    statement = select(Setting)
    result = await session.execute(statement)
    return result.scalars().all()


@router.post("/settings")
async def add_setting(setting: SettingCreate, session: AsyncSession = Depends(get_session)):
    db_setting = Setting.from_orm(setting)
    session.add(db_setting)
    await session.commit()
    await session.refresh(db_setting)
    return db_setting