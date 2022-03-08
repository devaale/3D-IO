import pstats
import uvicorn
import socketio

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession


from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from app.db import init_db, get_session

from app.core.config import Settings
from app.models.setting import Setting, SettingCreate


settings = Settings()

app = FastAPI()

sio = socketio.AsyncServer(
    async_mode=settings.SOCKET_ASYNC_MODE,
    cors_allowed_origins=settings.CORS_ALLOWED_ORIGINS,
)

sio_app = socketio.ASGIApp(sio)


@sio.event
async def connect(sid, environ):
    print("Disconnected...")


@sio.event
async def disconnect(sid):
    print("Connected...")


@app.on_event("startup")
async def on_startup():
    # await init_db()
    pass


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


@app.get("/settings", response_model=list[Setting])
async def get_settings(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Setting))
    return result.scalars().all()


@app.post("/settings")
async def add_setting(setting: SettingCreate, session: AsyncSession = Depends(get_session)):
    setting = Setting(label=setting.label, value=setting.value, min_value=setting.value,
                        max_value=setting.value, type=setting.type, measurement=setting.measurement)
    session.add(setting)
    await session.commit()
    await session.refresh(setting)
    return setting


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount(settings.SOCKET_MOUNT, sio_app)
