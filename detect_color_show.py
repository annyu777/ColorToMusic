import cv2
import numpy as np

#these bound is HSV
lowerBound_green = np.array([33, 80, 40])
upperBound_green = np.array([102, 255, 255])

lowerBound_red = np.array([0, 100, 100])
upperBound_red = np.array([5, 255, 255])

def detect_color_show(lowerBound, upperBound, song):
    cam = cv2.VideoCapture(0)
    kernelOpen = np.ones((5, 5))
    kernelClose = np.ones((20, 20))

    font = cv2.FONT_HERSHEY_SIMPLEX

    while True:
        ret, img = cam.read()
        img = cv2.resize(img, (512, 384))

        # convert BGR to HSV
        imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        #print (imgHSV)
        # create the Mask
        mask = cv2.inRange(imgHSV, lowerBound, upperBound)
        # morphology
        maskOpen = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernelOpen)
        maskClose = cv2.morphologyEx(maskOpen, cv2.MORPH_CLOSE, kernelClose)

        maskFinal = maskClose
        lala, conts, h = cv2.findContours(maskFinal.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        cv2.drawContours(img, conts, -1, (255, 0, 0), 3)
        for i in range(len(conts)):
            x, y, w, h = cv2.boundingRect(conts[i])
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(img, song, (x, y + h), font, 1.0, (0, 255, 255))
        #cv2.imshow("maskClose", maskClose)
        #cv2.imshow("maskOpen", maskOpen)
        #cv2.imshow("mask", mask)
        cv2.imshow("cam", img)
        cv2.waitKey(10)


detect_color_show(lowerBound_green, upperBound_green, "drum and trigger")
#detect_color_show(lowerBound_red, upperBound_red, "gtr1")