from app.models.result import ResultCreate
from app.crud.result import ResultCRUD
import pytest

from app.database.session import connect_test_db, ScopedSessionTest


@pytest.mark.asyncio
async def test_result_create():
    await connect_test_db()

    async with ScopedSessionTest() as session:
        result = await ResultCRUD().add(data=ResultCreate(), session=session)

    assert result is not None


@pytest.mark.asyncio
async def test_result_create():
    await connect_test_db()

    async with ScopedSessionTest() as session:
        _ = await ResultCRUD().add(data=ResultCreate(), session=session)
        result = await ResultCRUD().get(id=1, session=session)
    assert result is not None


@pytest.mark.asyncio
async def test_result_create():
    await connect_test_db()
    count = 0
    async with ScopedSessionTest() as session:
        _ = await ResultCRUD().add(data=ResultCreate(), session=session)
        _ = await ResultCRUD().add(data=ResultCreate(), session=session)
        _ = await ResultCRUD().add(data=ResultCreate(), session=session)

        result = await ResultCRUD().get_all(session=session)
        count = len(result)
    assert count == 3
