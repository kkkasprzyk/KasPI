

## Revision of code 27.04.2024 - Release 3 ##  -- > main.py module

### IMPORTANT IMPORTS ###

from config_kaspi import *
from picamera2 import Picamera2

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Usage: python main.py <video_path>')
        sys.exit()
    picam = Picamera2()
    picam.configure(picam.create_video_configuration(main={"format": "RGB888"}))
    picam.start()
    #video_path = sys.argv[1]
    video_path = picam.capture_array()
    print("video path: ", video_path)
    gui_kaspi(video_path,picam)

