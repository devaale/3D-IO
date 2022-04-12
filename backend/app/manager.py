from threading import Thread
from app.services.camera import CameraService


class Manager:
    def __init__(self) -> None:
        self._thread = None
        self._service: CameraService = CameraService()

    def start_service(self):
        if self._thread is None:
            self._thread = Thread(target=self._service.run)
            self._thread.setDaemon(True)
            self._thread.start()

    def trigger_service(self):
        self._service.set_manual_detect()
