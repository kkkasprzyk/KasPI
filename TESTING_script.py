import numpy as np

from config_kaspi import *
modul = YOLO("yolov8n.pt")
print(modul.names)


import numpy as np

# Pobieranie danych od użytkownika
x, y, z, t = map(int, input("Wprowadź dane w formacie 'start:koniec,start:koniec': ").split(','))

# Tworzenie tablicy zerowej o wymiarach (10, 10)
frame_list = np.zeros((10, 10))

# Wybieranie fragmentu tablicy na podstawie danych wprowadzonych przez użytkownika
selected_fragment = frame_list[x:y, z:t]

# Drukowanie otrzymanego fragmentu
print("Wybrany fragment tablicy:")
print(selected_fragment)

