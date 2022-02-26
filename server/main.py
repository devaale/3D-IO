from fastapi import FastAPI
import uvicorn
import socketio


app = FastAPI()
sio = socketio.AsyncServer(async_mode="asgi", cors_allowed_origins="*")
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
    return {"Hello": "World"}


@app.get("/test")
async def test():
    await show("Test page...")
    return {"Hello": "Test"}


async def show(message: str):
    print(message)

app.mount('/', sio_app)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host='127.0.0.1',
        port=5000,
        reload=True
    )