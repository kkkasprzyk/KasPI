## Revision of code 27.04.2024 - Release 3 ##  -- > config_kaspi.py module

import tkinter as tk
from PIL import Image, ImageTk
from ultralytics import YOLO
from ultralytics.solutions import object_counter
import cv2
import matplotlib.pyplot as plt
from select_point import select_line_points
from initialize_yolo_model import initialize_yolo_model
from gui_kaspi import gui_kaspi
import sys
