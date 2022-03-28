import socketio

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.seeder import seed_db
from app.database.session import connect_db, disconnect_db

from app.core.config import Settings
from app.crud.setting import CRUDSetting
from app.api.v1.router import router

settings = Settings()

app = FastAPI()

sio = socketio.AsyncServer(
    async_mode=settings.SOCKET_ASYNC_MODE,
    cors_allowed_origins=settings.CORS_ALLOWED_ORIGINS,
)

sio_app = socketio.ASGIApp(sio)


@app.on_event("startup")
async def on_startup():
    await connect_db()
    await seed_db()


@app.on_event("shutdown")
async def shutdown():
    await disconnect_db()


@sio.event
async def connect(sid, environ):
    print("Connected...")


@sio.event
async def disconnect(sid):
    print("Disconnected...")


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

app.include_router(router)

app.mount(settings.SOCKET_MOUNT, sio_app)
