from app.hardware.interfaces.service_base import Service
from app.hardware.enums.service_enum import ServiceType
from app.hardware.services.plc_service import PlcService
from app.hardware.services.cam_service import CameraService


class ServiceFactory:
    def create(self, service_type: ServiceType) -> Service:
        if service_type is ServiceType.PLC.value:
            return PlcService()
        elif service_type is ServiceType.CAMERA.value:
            return CameraService()
