import uvicorn
import socketio

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession


from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from app.db import init_db, get_session
from app.models import Song, SongCreate
from app.core.config import Settings

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
    pass


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


@app.get("/songs", response_model=list[Song])
async def get_songs(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Song))
    return result.scalars().all()


@app.post("/songs")
async def add_song(song: SongCreate, session: AsyncSession = Depends(get_session)):
    song = Song(name=song.name, artist=song.artist, year=song.year)
    session.add(song)
    await session.commit()
    await session.refresh(song)
    return song


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount(settings.SOCKET_MOUNT, sio_app)
