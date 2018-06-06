import cv2
import numpy as np

#this function take in a color and capture the current cam image with detection of the color-object
def detect_color_data(lowerBound,upperBound):
    cam = cv2.VideoCapture(0)
    kernelOpen = np.ones((5, 5))
    kernelClose = np.ones((20, 20))

    font = cv2.FONT_HERSHEY_SIMPLEX

    ret, img = cam.read()
    img = cv2.resize(img, (1024, 768))

    # convert BGR to HSV
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # create the Mask
    mask = cv2.inRange(imgHSV, lowerBound, upperBound)
    # morphology
    maskOpen = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernelOpen)
    maskClose = cv2.morphologyEx(maskOpen, cv2.MORPH_CLOSE, kernelClose)

    maskFinal = maskClose
    lala, conts, h = cv2.findContours(maskFinal.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    if len(conts) == 0 :
        x, y, w, h = [0, 0, 0, 0]
    else:
        x, y, w, h = cv2.boundingRect(conts[0])

    return x, y, w, h


#print(detect_color_data(lowerBound1,upperBound1))