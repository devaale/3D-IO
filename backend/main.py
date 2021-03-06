import socketio
import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.seeder import seed_db
from app.database.session import connect_db, disconnect_db, ScopedSession

from app.crud.setting import CRUDSetting

from app.common.config import Settings
from app.api.v1.router import router

from app.manager import ServiceManager

settings = Settings()

app = FastAPI()

sio = socketio.AsyncServer(
    async_mode=settings.SOCKET_ASYNC_MODE,
    cors_allowed_origins=settings.SOCKET_ORIGINS_ALLOWED,
)

sio_app = socketio.ASGIApp(sio)

manager = ServiceManager()


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
    async with ScopedSession() as session:
        await CRUDSetting.update_value(id=int(data["id"]), value=float(data["value"]))


@sio.event
async def set_algorithm(sid, data):
    algorithm_type = data["algorithm"]
    # manager.set_product_algorithm(algorithm_type)
    print(f"Setting algorithm {algorithm_type}")


@sio.event
async def detect(sid, data):
    await manager.detect()


@sio.event
async def train(sid, data):
    await manager.train()


@sio.event
async def update_product_model_selected(sid, data):
    pass


@sio.event
async def trigger(sid, data):
    await manager.camera_detect()


@sio.event
async def camera_start(sid, data):
    await manager.camera_start()


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ORIGINS_ALLOWED,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

app.mount(settings.SOCKET_MOUNT, sio_app)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")
