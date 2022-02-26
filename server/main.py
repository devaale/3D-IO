import uvicorn
from fastapi import FastAPI
import socketio


api = FastAPI()
sio = socketio.AsyncServer(async_mode="asgi", cors_allowed_origins="*")
app = socketio.ASGIApp(sio, api)


@sio.event
async def connect(sid, environ):
    await show("Connected...")


@sio.event
async def disconnect(sid):
    await show("Disconnected...")


@api.on_event("startup")
async def startup():
    await show("Starting up...")


@api.on_event("shutdown")
async def shutdown():
    await show("Shutting down...")


@api.get("/")
async def index():
    await show("Index page...")
    return {"Hello": "World"}


@api.get("/test")
async def test():
    await show("Test page...")
    return {"Hello": "World"}


async def show(message: str):
    print(message)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host='127.0.0.1',
        port=8000,
        reload=True
    )