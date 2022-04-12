import socketio
import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.seeder import seed_db
from app.database.session import connect_db, disconnect_db

from app.core.config import Settings
from app.api.v1.router import router
from threading import Thread
from app.services.camera import CameraService

settings = Settings()

app = FastAPI()

sio = socketio.AsyncServer(
    async_mode=settings.SOCKET_ASYNC_MODE,
    cors_allowed_origins=settings.SOCKET_ORIGINS_ALLOWED,
)

sio_app = socketio.ASGIApp(sio)

camera_service = CameraService()
camera_service_thread = None


@app.on_event("startup")
async def on_startup():
    await connect_db()
    await seed_db()
    global camera_service, camera_service_thread
    if camera_service_thread is None:
        camera_service_thread = Thread(target=camera_service.run)
        camera_service_thread.setDaemon(True)
        camera_service_thread.start()


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


@sio.event
async def trigger(sid, data):
    print(f"TRIGGER")
    global camera_service
    camera_service.set_manual_detect()


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
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, log_level="info")
