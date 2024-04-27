## Revision of code 27.04.2024 - Release 3 ##  -- > main.py module
from config_kaspi import *


def initialize_yolo_model(line_points,video_path):

    print("############### START MODULE initialize_yolo_model()  ##############")

### Initialize model of YOLO ####################
    yolo_model = YOLO("yolov8n.pt")
    yolo_model.conf =0.05 ## Reliability of model yolo
    video_to_process = cv2.VideoCapture(video_path)


    assert video_to_process.isOpened(), "Please provide a valid video path"


    w, h, fps = (int(video_to_process.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

    #line_points = select_line_points(video_path=video_path)  # line or region points

    classes_to_count = [0, 2]  # person and car classes for count

    # Video writer
    video_writer = cv2.VideoWriter("object_counting_output.avi",
                                   cv2.VideoWriter_fourcc(*'mp4v'),
                                   fps,
                                   (w, h))

    # Init Object Counter
    counter = object_counter.ObjectCounter()
    counter.set_args(view_img=True,
                     reg_pts=line_points,
                     classes_names=yolo_model.names,
                     )
    frame_count=0
    in_counts = []
    out_counts = []
    while video_to_process.isOpened():
        success = video_to_process.grab()  # Skip decoding, grab frame only
        if not success:
            break
        frame_count+=1
        if frame_count % 4 != 0:
            continue
        success, im0 = video_to_process.retrieve()  # Retrieve the grabbed frame and decode it
        if not success:
            break

        # Zmniejsz rozdzielczość obrazu
        im0 = cv2.resize(im0, (1920,1080))

        tracks = yolo_model.track(im0, persist=True, show=True,
                             classes=classes_to_count, verbose=True)

        im0 = counter.start_counting(im0, tracks)
        video_writer.write(im0)

        # Zapisz aktualne wartości in_counts i out_counts
        in_counts.append(counter.in_counts)
        out_counts.append(counter.out_counts)

        # Wyświetl wykres
        plt.plot(range(len(in_counts)), in_counts, label='In Counts')
        plt.plot(range(len(out_counts)), out_counts, label='Out Counts')
        plt.xlabel('Frame')
        plt.ylabel('Count')
        plt.title('Object Counts Over Time')
        plt.legend()
        plt.draw()
        plt.pause(0.01)  # Pozwól wykresowi zaktualizować się
        plt.clf()  # Wyczyść aktualny wykres, aby narysować nowy

    video_to_process.release()
    video_writer.release()
    cv2.destroyAllWindows()
    print("########   ###      KONIEC   ###     ###############")
