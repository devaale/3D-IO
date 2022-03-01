import uvicorn
import socketio

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import Settings

settings = Settings()

app = FastAPI()

origins = [
    "http://localhost:3000",
]

sio = socketio.AsyncServer(
    async_mode=settings.SOCKET_ASYNC_MODE,
    cors_allowed_origins=[],
)

sio_app = socketio.ASGIApp(sio)


@sio.event
async def connect(sid, environ):
    await show("Connected...")


@sio.event
async def disconnect(sid):
    await show("Disconnected...")


@app.on_event("startup")
async def startup():
    await show("Starting up...")


@app.on_event("shutdown")
async def shutdown():
    await show("Shutting down...")


@app.get("/")
async def index():
    await show("Index page...")
    return [{"id": "1", "name": "World"}, {"id": "2", "name": "Hello"}]


@app.get("/test")
async def test():
    await show("Test page...")
    return {"Hello": "Test"}


async def show(message: str):
    print(message)


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount(settings.SOCKET_MOUNT, sio_app)

if __name__ == "__main__":
    uvicorn.run(
        settings.ASGI_PROTOCOL,
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.ASGI_RELOAD,
    )
