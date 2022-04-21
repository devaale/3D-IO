from app.models.camera import Camera, CameraCreate
from sqlalchemy.ext.asyncio import AsyncSession


class CameraCRUD:
    def __init__(self) -> None:
        pass

    async def get(self, session: AsyncSession) -> Camera:
        return await session.get(Camera, 1)

    async def add(self, data: CameraCreate, session: AsyncSession) -> Camera:
        obj = Camera.from_orm(data)
        session.add(obj)
        await session.commit()
        await session.refresh(obj)
        return obj
