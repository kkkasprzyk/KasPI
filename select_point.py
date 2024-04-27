## Revision of code 27.04.2024 - Release 3 ##  -- > main.py module

from config_kaspi import *
def select_line_points(video_path):
    cap = cv2.VideoCapture(video_path)
    assert cap.isOpened(), "Error reading video file"

    # Ustaw domyślne wartości punktów linii
    line_points = [(20, 400), (1080, 400)]

    # Wyświetl pierwszą klatkę wideo i pozwól użytkownikowi wybrać punkty
    while True:
        success, frame = cap.read()
        if not success:
            print("Unable to read the first frame of the video.")
            break

        # Wyświetl obraz wideo
        frame = cv2.resize(frame,(1920,1080))
        cv2.imshow('Select Points', frame)

        # Czekaj na klawisz 'c' aby kontynuować
        key = cv2.waitKey(0)
        if key == ord('c'):
            # Zapisz punkty zaznaczone przez użytkownika
            print("Click on two points on the line to select them.")
            points = []

            # Funkcja do obsługi kliknięć myszą
            def mouse_callback(event, x, y, flags, params):
                if event == cv2.EVENT_LBUTTONDOWN:
                    points.append((x, y))
                    cv2.circle(frame, (x, y), 5, (0, 0, 255), -1)
                    cv2.imshow('Select Points', frame)

            cv2.setMouseCallback('Select Points', mouse_callback)

            # Czekaj na klawisz 'c' aby kontynuować
            key = cv2.waitKey(0)
            if key == ord('c'):
                if len(points) == 2:
                    line_points = points
                    break

    # Zamknij okno z wyborem punktów
    cv2.destroyAllWindows()

    return line_points