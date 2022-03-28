from app.database.session import ScopedSession

from app.crud.plc import CRUDPlc
from app.models.plc import PlcCreate

from app.crud.plc_block import CRUDPlcBlock
from app.crud.setting import CRUDSetting
from app.enums.plc_block import (
    PlcBlockMode,
    PlcBlockCommand,
    PlcBlockDataType,
    PlcBlockByteSize,
)
from app.models.plc_block import PlcBlockCreate
from app.models.setting import SettingCreate
from app.database.session import ScopedSession


async def seed_db() -> None:
    await seed_plc()
    await seed_plc_blocks()
    await seed_settings()
    async with ScopedSession() as session:
        data = await CRUDSetting.get_all(session)
        for x in data:
            print(x)


async def seed_plc() -> None:
    async with ScopedSession() as session:
        plc = PlcCreate()
        _ = await CRUDPlc.add(session=session, data=plc)


async def seed_settings() -> None:
    async with ScopedSession() as session:
        settings = [SettingCreate(), SettingCreate(), SettingCreate()]

        for setting in settings:
            _ = await CRUDSetting.add(session, setting)


async def seed_plc_blocks() -> None:
    async with ScopedSession() as session:
        db_num = 1
        blocks = [
            PlcBlockCreate(
                desc="Connection persistency flag / bit",
                offset=0,
                offset_bit=0,
                db_num=db_num,
                size=PlcBlockByteSize.BOOL,
                mode=PlcBlockMode.WRITE.value,
                data_type=PlcBlockDataType.BOOL.value,
                command=PlcBlockCommand.CONNECTED.value,
            ),
            PlcBlockCreate(
                desc="Camera trigger flag",
                offset=12,
                offset_bit=0,
                db_num=db_num,
                mode=PlcBlockMode.READ,
                size=PlcBlockByteSize.BOOL,
                data_type=PlcBlockDataType.BOOL,
                command=PlcBlockCommand.TRIGGER,
            ),
            PlcBlockCreate(
                desc="Camera trigger flag ACK",
                offset=0,
                offset_bit=1,
                db_num=db_num,
                mode=PlcBlockMode.WRITE,
                size=PlcBlockByteSize.BOOL,
                data_type=PlcBlockDataType.BOOL,
                command=PlcBlockCommand.TRIGGER,
            ),
            PlcBlockCreate(
                desc="Get product type",
                offset=10,
                offset_bit=0,
                db_num=db_num,
                mode=PlcBlockMode.READ,
                size=PlcBlockByteSize.INT,
                data_type=PlcBlockDataType.INT,
                command=PlcBlockCommand.PRODUCT,
            ),
            PlcBlockCreate(
                desc="Get product type ACK",
                offset=2,
                offset_bit=0,
                db_num=db_num,
                mode=PlcBlockMode.WRITE,
                size=PlcBlockByteSize.INT,
                data_type=PlcBlockDataType.INT,
                command=PlcBlockCommand.PRODUCT,
            ),
            PlcBlockCreate(
                desc="Learning mode enable",
                offset=12,
                offset_bit=1,
                db_num=db_num,
                mode=PlcBlockMode.READ,
                size=PlcBlockByteSize.BOOL,
                data_type=PlcBlockDataType.BOOL,
                command=PlcBlockCommand.LEARN_MODE,
            ),
            PlcBlockCreate(
                desc="Learning mode enable ACK",
                offset=4,
                offset_bit=1,
                db_num=db_num,
                mode=PlcBlockMode.WRITE,
                size=PlcBlockByteSize.BOOL,
                data_type=PlcBlockDataType.BOOL,
                command=PlcBlockCommand.LEARN_MODE,
            ),
            PlcBlockCreate(
                desc="Check template for item exists",
                offset=4,
                offset_bit=2,
                db_num=db_num,
                mode=PlcBlockMode.WRITE,
                size=PlcBlockByteSize.BOOL,
                data_type=PlcBlockDataType.BOOL,
                command=PlcBlockCommand.MODEL_EXIST,
            ),
            PlcBlockCreate(
                desc="Set result correct / wrong",
                offset=6,
                offset_bit=0,
                db_num=db_num,
                mode=PlcBlockMode.WRITE,
                size=PlcBlockByteSize.BOOL,
                data_type=PlcBlockDataType.BOOL,
                command=PlcBlockCommand.RESULT,
            ),
            PlcBlockCreate(
                desc="Data processing is done",
                offset=4,
                offset_bit=0,
                db_num=db_num,
                mode=PlcBlockMode.WRITE,
                size=PlcBlockByteSize.BOOL,
                data_type=PlcBlockDataType.BOOL,
                command=PlcBlockCommand.PROCESSING_DONE,
            ),
        ]

        for block in blocks:
            _ = await CRUDPlcBlock.add(session=session, data=block)
