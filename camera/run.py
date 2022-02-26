import random

from enums.camera_type import CameraType

from camera_creator import CameraCreator
from D435_creator import RealSenseD435Creator
from D435i_creator import RealSenseD435iCreator

def main(creator: CameraCreator = None):
    for _ in range(3):

        enum = random.choice(list(CameraType))

        if enum is CameraType.RealSenseD435:
            creator = RealSenseD435Creator()

        elif enum is CameraType.RealSenseD453i:
            creator = RealSenseD435iCreator()
        
        else:
            continue
        
        camera = creator.create_camera().start()

if __name__ == '__main__':
    main()
