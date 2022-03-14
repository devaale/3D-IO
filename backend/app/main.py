import uvicorn
import socketio

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db import init_db

from app.api import setting, plc, plc_block
from app.core.config import Settings

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


@app.on_event("shutdown")
async def shutdown():
    pass


@sio.event
async def connect(sid, environ):
    print("Connected...")


@sio.event
async def disconnect(sid):
    print("Disconnected...")


# TODO: Find a way to parse event data to an object
@sio.event
async def update_setting(sid, data):
    new_value = data["value"]
    print(f"Updating setting: {new_value}")


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(setting.router)
app.include_router(plc.router)
app.include_router(plc_block.router)

app.mount(settings.SOCKET_MOUNT, sio_app)
