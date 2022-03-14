import time
from app.hardware.interfaces.service_base import Service


class PlcService(Service):
    def run(self):
        while self.running:
            time.sleep(1)
            print("PLC Data")

    def stop(self):
        self.running = False
