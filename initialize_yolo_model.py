## Revision of code 27.04.2024 - Release 3 ##  -- > main.py module
import plotter
from config_kaspi import *


def initialize_yolo_model(line_points,video_path,slow_factor,x_resolution,y_resolution):

    print("############### START MODULE initialize_yolo_model()  ##############")

### Initialize model of YOLO ####################

    yolo_model = YOLO("yolov3.pt")
    yolo_model.conf =0.05 ## Reliability of model yolo
    video_to_process = cv2.VideoCapture(video_path)
    assert video_to_process.isOpened(), "Please provide a valid video path"
    w, h, fps = (int(video_to_process.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
    classes_to_count = [0, 2]  # person and car classes for count


    # Init Object Counter
    counter = object_counter.ObjectCounter()
    counter.set_args(view_img=True,
                     reg_pts=line_points,
                     classes_names=yolo_model.names,
                     )


    #################### Function to slowing down video #################################################
    frame_count=0
    in_counts = []
    out_counts = []
    while video_to_process.isOpened():
        success = video_to_process.grab()  # Skip decoding, grab frame only
        if not success:
            break
        frame_count+=1
        if frame_count % slow_factor != 0:
            continue
        success, im0 = video_to_process.retrieve()  # Retrieve the grabbed frame and decode it
        if not success:
            break
    #########################################################################################################


    #############################  TRACKING OBJECT #######################################################################
        im0 = cv2.resize(im0, (x_resolution,y_resolution))
        tracks = yolo_model.track(im0, persist=True, show=True,
                             classes=classes_to_count, verbose=True,conf=yolo_model.conf)
        im0 = counter.start_counting(im0, tracks)
    ######################################################################################################

        plot_count_object(counter=counter)

    #### ENDING OF PROCESS #################
    video_to_process.release()
    cv2.destroyAllWindows()
    print("########   ###      KONIEC   ###     ###############")
    ###################################################################

def plot_count_object(counter):
    plotter.plotter(counter.class_wise_count['perso']['in'], counter.class_wise_count['perso']['out'],'PERSON',1)  ## ploting x,y axis graph
    plotter.plotter(counter.class_wise_count['car']['in'], counter.class_wise_count['car']['out'],'CAR',2)  ## ploting x,y axis graph