

## Revision of code 25.04.2024 - Release 1 ##  -- > main.py module

### IMPORTANT IMPORTS ###

from config_kaspi import *
## ### ### ### ### ### ###




if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Usage: python main.py <video_path>')
        sys.exit()

    video_path = sys.argv[1]
    gui_kaspi(video_path)

