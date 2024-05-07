## Revision of code 27.04.2024 - Release 3 ##  -- > main.py module
import plotter
from config_kaspi import *
import openpyxl
from openpyxl import Workbook
from datetime import datetime
import os
from result_to_excel import if_excel_exist,save_results_to_excel
project_path = os.getcwd()
excel_file_name = "results1.xlsx"
excel_file_name2 = "results2.xlsx"
file_path = os.path.join(project_path, excel_file_name)
file_path2 = os.path.join(project_path, excel_file_name2)

# Tworzymy plik Excel, jeśli nie istnieje
if_excel_exist(file_path)
if_excel_exist(file_path2)
def initialize_yolo_model(line_points,video_path,slow_factor,x_resolution,y_resolution):

    print("############### START MODULE initialize_yolo_model()  ##############")

### Initialize model of YOLO ####################

    yolo_model = YOLO("yolov8n.pt")
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
        video_duration = f"{frame_count / fps:.2f} seconds"
        plot_count_object_safe(counter,'perso',1)
        plot_count_object_safe(counter, 'car', 2)

        save_results_to_excel(file_path,counter.class_wise_count['car']['out'],counter.class_wise_count['car']['in'],video_duration)
        save_results_to_excel(file_path2, counter.class_wise_count['perso']['out'], counter.class_wise_count['perso']['in'],video_duration)


    #### ENDING OF PROCESS #################
    video_to_process.release()
    cv2.destroyAllWindows()
    print("########   ###      KONIEC   ###     ###############")
    ###################################################################

def plot_count_object_safe(counter,object_to_detect,figure):
    try:
        plotter.plotter(counter.class_wise_count[object_to_detect]['in'], counter.class_wise_count[object_to_detect]['out'],object_to_detect,figure)  ## ploting x,y axis graph
        print(counter.class_wise_count[object_to_detect]['in'],"-in->",object_to_detect)
        print(counter.class_wise_count[object_to_detect]['out'], "-out->", object_to_detect)

    except KeyError:
        print("KeyError->",object_to_detect)