import cv2
import numpy as np
from detect_color_show import detect_color_show

lowerBound_green = np.array([33, 80, 40])
upperBound_green = np.array([102, 255, 255])

lowerBound_red = np.array([0, 100, 100])
upperBound_red = np.array([5, 255, 255])
