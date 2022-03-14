import time
from app.hardware.interfaces.service_base import Service


class CameraService(Service):
    def run(self):
        while self.running:
            time.sleep(1)
            print("Camera service")

    def stop(self):
        self.running = False
