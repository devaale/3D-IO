from app.hardware.enums.service_enum import ServiceType
from app.hardware.factories.service_factory import ServiceFactory
import time

if __name__ == "__main__":
    service_types = ServiceType.get_values()
    factory = ServiceFactory()

    services = []
    for service_type in service_types:
        service = factory.create(service_type)
        services.append(service)

    for service in services:
        service.start()

    count = 0
    while count < 10:
        time.sleep(1)
        count += 1

    for service in services:
        service.stop()
