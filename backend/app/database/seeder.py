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
from app.enums.setting import MeasurementType
from app.models.setting import SettingCreate
from app.models.product import ProductCreate
from app.models.result import ResultCreate
from app.models.position import PositionModelCreate
from app.enums.product import (
    ClusteringAlgorithm,
    PlaneSegmentationAlgorithm,
    ProcessingCommand,
)
from app.crud.product import ProductCRUD


async def seed_db() -> None:
    await seed_products()
    await seed_plc()
    await seed_plc_blocks()
    await seed_settings()


async def seed_products() -> None:
    models = [
        ProductCreate(
            product="TEST_0",
            row_count=1,
            col_count=3,
            current=True,
            created=False,
            command=ProcessingCommand.TRAIN,
            clustering=ClusteringAlgorithm.DBSCAN,
            segmentation=PlaneSegmentationAlgorithm.RANSAC,
        )
    ]

    for model in models:
        _ = await ProductCRUD().create(model)


async def seed_plc() -> None:
    plc = PlcCreate()
    _ = await CRUDPlc().add(data=plc)


async def seed_settings() -> None:
    settings = [
        SettingCreate(
            key="accuracy",
            description="Accuracy (mm)",
            value=1.4,
            min_value=1,
            max_value=5,
            step=0.1,
            measurement=MeasurementType.MILLIMETERS,
        ),
        SettingCreate(
            key="corner_size",
            description="ROI size (%)",
            value=35,
            min_value=0,
            max_value=100,
            step=1,
            measurement=MeasurementType.PRECENTAGE,
        ),
        SettingCreate(
            key="distance_ground",
            description="Distance to ground (mm)",
            value=345,
            min_value=200,
            max_value=500,
            step=1,
            measurement=MeasurementType.MILLIMETERS,
        ),
        SettingCreate(
            key="depth_from",
            description="From depth (mm)",
            value=270,
            min_value=150,
            max_value=500,
            step=1,
            measurement=MeasurementType.MILLIMETERS,
        ),
        SettingCreate(
            key="depth_to",
            description="To depth (mm)",
            value=333,
            min_value=150,
            max_value=500,
            step=1,
            measurement=MeasurementType.MILLIMETERS,
        ),
        SettingCreate(
            key="cluster_min_size_precentage",
            description="Min cluster size (%)",
            value=65,
            min_value=0,
            max_value=100,
            step=1,
            measurement=MeasurementType.PRECENTAGE,
        ),
        SettingCreate(
            key="voxel_size",
            description="Voxel size (mm)",
            value=2.5,
            min_value=0,
            max_value=5,
            step=0.1,
            measurement=MeasurementType.MILLIMETERS,
        ),
        SettingCreate(
            key="crop_precentage_x",
            description="Crop X (%)",
            value=90,
            min_value=0,
            max_value=100,
            step=1,
            measurement=MeasurementType.PRECENTAGE,
        ),
        SettingCreate(
            key="crop_precentage_y",
            description="Crop Y (%)",
            value=100,
            min_value=0,
            max_value=100,
            step=1,
            measurement=MeasurementType.PRECENTAGE,
        ),
        SettingCreate(
            key="crop_precentage_z",
            description="Crop Z (%)",
            value=100,
            min_value=0,
            max_value=100,
            step=1,
            measurement=MeasurementType.PRECENTAGE,
        ),
    ]

    for setting in settings:
        _ = await CRUDSetting().add(data=setting)


async def seed_plc_blocks() -> None:
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
        _ = await CRUDPlcBlock().add(data=block)
