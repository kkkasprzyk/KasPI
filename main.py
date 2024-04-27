

## Revision of code 27.04.2024 - Release 3 ##  -- > main.py module

### IMPORTANT IMPORTS ###

from config_kaspi import *



if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Usage: python main.py <video_path>')
        sys.exit()

    video_path = sys.argv[1]
    print("video path: ", video_path)
    gui_kaspi(video_path)

