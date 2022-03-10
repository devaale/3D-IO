import uvicorn
import socketio

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession


from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.db import init_db, get_session

from app.core.config import Settings
from app.models.setting import Setting, SettingCreate, SettingDelete

settings = Settings()

app = FastAPI()

sio = socketio.AsyncServer(
    async_mode=settings.SOCKET_ASYNC_MODE,
    cors_allowed_origins=settings.CORS_ALLOWED_ORIGINS,
)

sio_app = socketio.ASGIApp(sio)

@app.on_event("startup")
async def on_startup():
    await init_db()

@sio.event
async def connect(sid, environ):
    print("Connected...")


@sio.event
async def disconnect(sid):
    print("Disconnected...")

#TODO: Find a way to parse event data to an object
@sio.event
async def update_setting(sid, data):
    new_value = data["value"]
    print(f'Updating setting: {new_value}')


@app.delete("/settings/{id}", response_model=SettingDelete)
async def delete_setting(id, session: AsyncSession = Depends(get_session)):
    db_setting = await session.get(Setting, id)

    if not db_setting:
        raise HTTPException(status_code=404, detail="Setting not found")
    
    await session.delete(db_setting)
    await session.commit()
    return db_setting


@app.get("/settings", response_model=list[Setting])
async def get_settings(session: AsyncSession = Depends(get_session)):
    statement = select(Setting)
    result = await session.execute(statement)
    return result.scalars().all()


@app.post("/settings")
async def add_setting(setting: SettingCreate, session: AsyncSession = Depends(get_session)):
    db_setting = Setting.from_orm(setting)
    session.add(db_setting)
    await session.commit()
    await session.refresh(db_setting)
    return db_setting

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount(settings.SOCKET_MOUNT, sio_app)
