from dataclasses import dataclass

from camera import Camera

@dataclass
class RealSenseD453i(Camera):
    width: int = 10
    height: int = 10
    
    def start(self):
        print("Starting RealSenseD453i")
    

    def stop(self):
        print("Stopping RealSenseD453i")

    
    def __del__(self):
        self.stop()