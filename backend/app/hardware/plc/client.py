import snap7
from threading import Lock

from app.models.plc import Plc
from app.models.plc_block import PlcBlock


class PlcClientAdapter:
    def __init__(self, plc: Plc):
        self.__plc = plc
        self.__lock = Lock()
        self.__client = snap7.client.Client()

    # TODO: Add try / except blocks
    def connect(self) -> bool:
        with self.__lock:
            self.__client.connect(self.__plc.ip, self.__plc.rack, self.__plc.slot)

        return self.connected()

    def connected(self) -> bool:
        with self.__lock:
            return self.__client.get_connected()

    def disconnect(self) -> bool:
        with self.__lock:
            self.__client.disconnect()

        return self.connected()

    def execute(self, block: PlcBlock):
        # TODO: Create plc command factory
        # command = PlcCommandFactory.create(block.type)
        # converter = PlcConverterFactory.create(block.data_type)

        # command.set_converter(converter)
        # command.execute()
        pass
