from dataclasses import dataclass
from camera import Camera

@dataclass
class RealSenseD453(Camera):
    width: int = 10
    height: int = 10

    def start(self):
        print("Starting RealSenseD453")
    

    def stop(self):
        print("Stopping RealSenseD453")

    
    def __del__(self):
        self.stop()