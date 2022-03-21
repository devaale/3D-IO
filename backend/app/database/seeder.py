from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import ScopedSession

from app.crud.plc import CRUDPlc
from app.models.plc import PlcCreate

from app.crud.plc_block import CRUDPlcBlock
from app.enums.plc_block import (
    PlcBlockMode,
    PlcBlockCommand,
    PlcBlockDataType,
    PlcBlockDataTypeSize,
)
from app.models.plc_block import PlcBlockCreate


async def seed_db() -> None:
    await seed_plc()
    await seed_plc_blocks()


async def seed_plc() -> None:
    async with ScopedSession() as session:
        # TODO: Add actual PLC data
        plc = PlcCreate()
        _ = await CRUDPlc.add(session=session, data=plc)


async def seed_plc_blocks() -> None:
    async with ScopedSession() as session:
        db_num = 1
        blocks = [
            PlcBlockCreate(
                desc="Connection persistency flag / bit",
                offset=0,
                offset_bit=0,
                db_num=db_num,
                size=PlcBlockDataTypeSize.BOOL,
                mode=PlcBlockMode.WRITE.value,
                data_type=PlcBlockDataType.BOOL.value,
                command=PlcBlockCommand.CONN_EXIST.value,
            ),
            PlcBlockCreate(
                desc="Camera trigger flag",
                offset=12,
                offset_bit=0,
                db_num=db_num,
                mode=PlcBlockMode.READ,
                size=PlcBlockDataTypeSize.BOOL,
                data_type=PlcBlockDataType.BOOL,
                command=PlcBlockCommand.TRIGGER_CAM,
            ),
            PlcBlockCreate(
                desc="Camera trigger flag ACK",
                offset=0,
                offset_bit=1,
                db_num=db_num,
                mode=PlcBlockMode.WRITE,
                size=PlcBlockDataTypeSize.BOOL,
                data_type=PlcBlockDataType.BOOL,
                command=PlcBlockCommand.TRIGGER_CAM,
            ),
            PlcBlockCreate(
                desc="Get product type",
                offset=10,
                offset_bit=0,
                db_num=db_num,
                mode=PlcBlockMode.READ,
                size=PlcBlockDataTypeSize.INT,
                data_type=PlcBlockDataType.INT,
                command=PlcBlockCommand.PRODUCT_GET,
            ),
            PlcBlockCreate(
                desc="Get product type ACK",
                offset=2,
                offset_bit=0,
                db_num=db_num,
                mode=PlcBlockMode.WRITE,
                size=PlcBlockDataTypeSize.INT,
                data_type=PlcBlockDataType.INT,
                command=PlcBlockCommand.PRODUCT_GET,
            ),
            PlcBlockCreate(
                desc="Learning mode enable",
                offset=12,
                offset_bit=1,
                db_num=db_num,
                mode=PlcBlockMode.READ,
                size=PlcBlockDataTypeSize.BOOL,
                data_type=PlcBlockDataType.BOOL,
                command=PlcBlockCommand.LEARN_MODE_ON,
            ),
            PlcBlockCreate(
                desc="Learning mode enable ACK",
                offset=4,
                offset_bit=1,
                db_num=db_num,
                mode=PlcBlockMode.WRITE,
                size=PlcBlockDataTypeSize.BOOL,
                data_type=PlcBlockDataType.BOOL,
                command=PlcBlockCommand.LEARN_MODE_ON,
            ),
            PlcBlockCreate(
                desc="Check template for item exists",
                offset=4,
                offset_bit=2,
                db_num=db_num,
                mode=PlcBlockMode.WRITE,
                size=PlcBlockDataTypeSize.BOOL,
                data_type=PlcBlockDataType.BOOL,
                command=PlcBlockCommand.TEMPLATE_EXIST,
            ),
            PlcBlockCreate(
                desc="Set result correct / wrong",
                offset=6,
                offset_bit=0,
                db_num=db_num,
                mode=PlcBlockMode.WRITE,
                size=PlcBlockDataTypeSize.BOOL,
                data_type=PlcBlockDataType.BOOL,
                command=PlcBlockCommand.RESULT_SET,
            ),
            PlcBlockCreate(
                desc="Data processing is done",
                offset=4,
                offset_bit=0,
                db_num=db_num,
                mode=PlcBlockMode.WRITE,
                size=PlcBlockDataTypeSize.BOOL,
                data_type=PlcBlockDataType.BOOL,
                command=PlcBlockCommand.PROC_DONE_SET,
            ),
        ]

        for block in blocks:
            _ = await CRUDPlcBlock.add(session=session, data=block)
